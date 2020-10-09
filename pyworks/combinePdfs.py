#! python3
# combinePdfs.py - 指定したフォルダのすべてのPDFを一つのPDFにする

import PyPDF2, os

os.chdir(input(r"PDFファイルのあるフォルダのパスを入力してください"))

# すべてのPDFファイル名を取得する
pdf_files = []
for filename in os.listdir("."):    # カレントディレクトリのすべてのファイルのリストからひとつずつ取り出す
    if filename.endswith(".pdf"):   # PDFファイルなら
        pdf_files.append(filename)  # PDFファイルのリストに追加

pdf_files.sort(key=str.lower)       # アルファベット順に並び替え

pdf_writer = PyPDF2.PdfFileWriter() # PdfFIleWriterオブジェクトを生成

# すべてのPDFファイルをループする
for filename in pdf_files:
    pdf_file_obj = open(filename,"rb")
    pdf_reader = PyPDF2.PdfFileReader(pdf_file_obj) # 一つずつPdfFileReaderオブジェクトを生成する
    
    # 先頭のページを除いたすべてのページを追加する
    for page_num in range(1,pdf_reader.numPages):
        page_obj = pdf_reader.getPage(page_num)     # 先頭ページを除いてPageオブジェクトを生成し
        pdf_writer.addPage(page_obj)                # PdfFileWriterオブジェクトに追加する

# 結合したPDFをファイルに保存する
pdf_output = open(r"..\join_pdf.pdf", "wb")
pdf_writer.write(pdf_output)
print("{pdf_output}を作成しました")
pdf_output.close()