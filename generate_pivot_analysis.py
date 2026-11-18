import pandas as pd

def main():
    df = pd.read_csv("data/corporate_sales_procurement_2024.csv")
    print("=== Ringkasan Pivot Table: Total Nilai Pengadaan (IDR) per Departemen & Produk ===")
    pivot_val = pd.pivot_table(
        df,
        values="Total_Amount_IDR",
        index="Department",
        columns="Product",
        aggfunc="sum",
        fill_value=0,
        margins=True,
        margins_name="Total"
    )
    print(pivot_val)

    print("\n=== Ringkasan Pivot Table: Total Unit Kuantitas per Departemen & Kuartal ===")
    pivot_qty = pd.pivot_table(
        df,
        values="Quantity",
        index="Department",
        columns="Quarter",
        aggfunc="sum",
        fill_value=0,
        margins=True,
        margins_name="Total_Unit"
    )
    print(pivot_qty)

if __name__ == "__main__":
    main()
