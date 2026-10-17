from tools import (
    get_sales_data,
    get_total_sales,
    get_lowest_sales_product,
    get_highest_sales_product,
)


def test_sales_data_not_empty():
    assert get_sales_data()


def test_total_sales():
    result = get_total_sales()
    assert "775,000" in result


def test_lowest_sales_product():
    result = get_lowest_sales_product()
    assert "Keyboard" in result


def test_highest_sales_product():
    result = get_highest_sales_product()
    assert "Laptop" in result