from pathlib import Path
import pandas as pd

RAW_DIR = Path("/opt/airflow/data/raw")
PROCESSED_DIR = Path("/opt/airflow/data/processed")

INPUT_FILE = RAW_DIR / "retail_sales.csv"
OUTPUT_FILE = PROCESSED_DIR / "cleaned_retail_sales.csv"


def normalize_column_names(df: pd.DataFrame) -> pd.DataFrame:
    df.columns = [
        col.strip().lower().replace(" ", "_").replace("-", "_")
        for col in df.columns
    ]
    return df


def main():
    PROCESSED_DIR.mkdir(parents=True, exist_ok=True)

    if not INPUT_FILE.exists():
        raise FileNotFoundError(f"Input file not found: {INPUT_FILE}")

    df = pd.read_csv(INPUT_FILE)
    print(f"Raw shape: {df.shape}")

    # Normalize headers
    df = normalize_column_names(df)

    # Strip whitespace from string columns
    string_cols = ["region", "category", "product"]
    for col in string_cols:
        if col in df.columns:
            df[col] = df[col].astype(str).str.strip()

    # Parse date column
    df["order_date"] = pd.to_datetime(df["order_date"], errors="coerce")

    # Enforce numeric types
    numeric_cols = ["sales", "quantity", "profit"]
    for col in numeric_cols:
        df[col] = pd.to_numeric(df[col], errors="coerce")

    # Drop rows missing required fields
    required_cols = [
        "order_id",
        "order_date",
        "region",
        "category",
        "product",
        "sales",
        "quantity",
        "profit",
    ]
    df = df.dropna(subset=required_cols)

    # Remove duplicates
    df = df.drop_duplicates(subset=["order_id"]).reset_index(drop=True)

    # Remove impossible values
    df = df[(df["sales"] >= 0) & (df["quantity"] > 0)]

    # Feature engineering
    df["year"] = df["order_date"].dt.year
    df["month"] = df["order_date"].dt.month
    df["month_name"] = df["order_date"].dt.month_name()
    df["quarter"] = df["order_date"].dt.quarter
    df["day_name"] = df["order_date"].dt.day_name()

    df["profit_margin"] = (df["profit"] / df["sales"]).round(4)
    df["avg_selling_price"] = (df["sales"] / df["quantity"]).round(2)

    # Optional text field for future RAG / LLM use
    df["sales_summary"] = df.apply(
        lambda row: (
            f"Order {int(row['order_id'])} was placed on {row['order_date'].date()} "
            f"in the {row['region']} region for category {row['category']}. "
            f"Product: {row['product']}. Sales: {row['sales']}, "
            f"Quantity: {int(row['quantity'])}, Profit: {row['profit']}."
        ),
        axis=1,
    )

    # Sort by date
    df = df.sort_values(by="order_date").reset_index(drop=True)

    print(f"Cleaned shape: {df.shape}")
    print("Columns in cleaned file:")
    print(df.columns.tolist())

    df.to_csv(OUTPUT_FILE, index=False)
    print(f"Saved cleaned file to: {OUTPUT_FILE}")


if __name__ == "__main__":
    main()