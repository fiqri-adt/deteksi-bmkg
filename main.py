"""
Aplikasi deteksi gempa terkini
MODULARISASI DENGAN FUNCTION
MODULARISASI DENGAN PACKAGE
"""
from gempaterkini import ekstrasi_data, tampilkan_data

if __name__ == '__main__':
    print('aplikasi utama')
    result = ekstrasi_data()
    tampilkan_data(result)
