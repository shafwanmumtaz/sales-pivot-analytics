# Analisis Penjualan Korporat & Kinerja Pengadaan Departemen (Pivot Table Analytics)

👤 **Penyusun:** Shafwan Mumtaz  
📊 **Tools:** Microsoft Excel (Pivot Table, Fungsi Agregasi) & Python (`pandas`)

---

## 1. Deskripsi Studi Kasus

Proyek ini mengevaluasi data transaksi pengadaan perangkat keras IT sepanjang tahun **2024** yang tersebar pada **5 departemen perusahaan**:
- **IT**
- **Sales**
- **Marketing**
- **Finance**
- **HR (Human Resources)**

Serta mencakup **6 kategori produk utama**: *Laptop, Monitor, Keyboard, Phone, Tablet,* dan *Mouse*.

---

## 2. Metodologi Analisis

1. **Penyusunan Struktur Tabel Transaksi:** Memastikan atribut tanggal transaksi (`Date`), kuartal (`Quarter`), departemen (`Department`), kategori perangkat (`Product`), kuantitas (`Quantity`), harga satuan (`Unit_Price_IDR`), dan total nilai pengadaan (`Total_Amount_IDR`) terformat secara konsisten.
2. **Pembuatan Pivot Table Dinamis:**
   - Mengelompokkan total anggaran dan kuantitas unit berdasarkan **Departemen** (Baris) dan **Kategori Produk** (Kolom).
   - Membandingkan distribusi pengeluaran per kuartal (**Q1–Q4 2024**) untuk melihat periode puncak pengadaan.
3. **Evaluasi Efisiensi Anggaran:** Mengidentifikasi departemen dan kategori perangkat dengan penyerapan anggaran terbesar sebagai dasar perencanaan pengadaan tahun berikutnya.

---

## 3. Ringkasan Temuan Utama

- **Departemen IT & Sales** menyerap porsi anggaran perangkat terbesar, terutama didominasi oleh kebutuhan **Laptop** dan **Monitor** untuk mendukung produktivitas kerja teknis dan mobilitas tim penjualan.
- **Perangkat Pendukung (*Keyboard & Mouse*)** memiliki frekuensi permintaan unit yang merata di seluruh departemen namun dengan porsi biaya yang jauh lebih rendah.
- Rekapitulasi berbasis **Pivot Table** memangkas waktu penyusunan laporan lintas divisi dan memudahkan manajemen memantau realisasi anggaran per kuartal.

---

## 4. Struktur File

```text
├── data/
│   ├── corporate_sales_procurement_2024.csv   # Dataset transaksi pengadaan lintas 5 departemen (2024)
│   └── pivot_summary_by_department.csv        # Tabel hasil agregasi Pivot (Departemen x Produk)
├── generate_pivot_analysis.py                 # Skrip Python untuk mereproduksi tabel Pivot secara otomatis
└── README.md                                  # Dokumentasi proyek
```
