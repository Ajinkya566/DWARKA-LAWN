from pathlib import Path
import pandas as pd


DATA_FILE = Path(__file__).parent / "data" / "sales_data.csv"


def load_sales_data():
    """Load sales records from CSV."""

    if not DATA_FILE.exists():
        raise FileNotFoundError(
            f"Sales CSV not found: {DATA_FILE}"
        )

    df = pd.read_csv(DATA_FILE)

    required_columns = {
        "product",
        "region",
        "month",
        "sales",
        "units"
    }

    missing = required_columns - set(df.columns)

    if missing:
        raise ValueError(
            f"Missing CSV columns: {', '.join(sorted(missing))}"
        )

    return df


def get_sales_data():
    df = load_sales_data()
    return df.to_string(index=False)


def get_total_sales():
    df = load_sales_data()
    total = df["sales"].sum()

    return f"Total sales are ₹{total:,.0f}"


def get_lowest_sales_product():
    df = load_sales_data()
    row = df.loc[df["sales"].idxmin()]

    return (
        f"Lowest selling product is {row['product']} "
        f"with sales of ₹{row['sales']:,.0f}"
    )


def get_highest_sales_product():
    df = load_sales_data()
    row = df.loc[df["sales"].idxmax()]

    return (
        f"Highest selling product is {row['product']} "
        f"with sales of ₹{row['sales']:,.0f}"
    )