import mysql.connector

db = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='mini_market'
)

def insert_item(kode_barang, nama_barang, harga_barang, stok_barang):
    cursor = db.cursor()
    cursor.execute("INSERT INTO tbl_barang (kode_barang, nama_barang, harga_barang, stok_barang) VALUES (%s, %s, %s, %s)", (kode_barang, nama_barang, harga_barang, stok_barang))
    db.commit()
    
    if cursor.rowcount > 0:
        print("\nData berhasil dimasukan\n")
    else:
        print("\nData gagal di insert\n")
        
def fetch_item():
    cursor = db.cursor()
    cursor.execute("SELECT * FROM tbl_barang")
    return cursor.fetchall()

def delete_item(kode_barang):
    cursor = db.cursor()
    cursor.execute("DELETE FROM tbl_barang WHERE kode_barang = %s", (kode_barang,))
    db.commit()
    
def update_item(kode_barang, nama_barang=None, harga_barang=None, stok_barang=None):
        
        cursor = db.cursor()

        # Check if the item exists
        cursor.execute("SELECT * FROM tbl_barang WHERE kode_barang = %s", (kode_barang,))
        item = cursor.fetchone()

        if item is None:
            print(f"Barang dengan kode {kode_barang} tidak ditemukan.")
            return

        # SQL Update Query with Dynamic Fields
        update_fields = []
        params = []

        if nama_barang is not None:
            update_fields.append("nama_barang = %s")
            params.append(nama_barang)

        if harga_barang is not None:
            update_fields.append("harga_barang = %s")
            params.append(harga_barang)

        if stok_barang is not None:
            update_fields.append("stok_barang = %s")
            params.append(stok_barang)

        params.append(kode_barang)

        update_query = f"""
        UPDATE tbl_barang
        SET {', '.join(update_fields)}
        WHERE kode_barang = %s
        """

        # Execute the update query
        cursor.execute(update_query, tuple(params))
        
        db.commit()
        
        print(f"Barang dengan kode {kode_barang} telah diupdate.")
    
