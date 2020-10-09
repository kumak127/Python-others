#! python3
# encrypted.py - フォルダの中のすべてのPDFファイルを探し出し指定されたパスワードで暗号化する

import PyPDF2, os, sys

folder_path = input(r"暗号化したいPDFファイルがあるフォルダを入力してください:")
if len(sys.argv) > 1:
    password = sys.argv[1]

else:
    password = input("設定するパスワードを入れてください：")

# フォルダの中を歩いて、PDFファイルが見つかれば、すべてをコピーした後に暗号化し、ファイル名の後に_encrypted.pdfをつけて保存
for foldername, subfolders, filenames in os.walk(folder_path):
    for filename in filenames:
        if filename.endswith(".pdf"):
            pdf_reader = PyPDF2.PdfFileReader(open(os.path.join(foldername, filename), "rb"))
            pdf_writer = PyPDF2.PdfFileWriter()
            if pdf_reader.isEncrypted:
                continue
            for num_page in range(pdf_reader.numPages):
                pdf_writer.addPage(pdf_reader.getPage(num_page))
            filename_split_list = filename.split(".")
            new_filename = filename_split_list[0] + "_encrypted.pdf"
            pdf_writer.encrypt(password)
            print(os.path.join(foldername,new_filename)+"を作成しました")  # 使うときはここを消して下のコードのコメントを外す
            # pdf_writer.write(open(os.path.join(foldername,new_filename),"wb"))
            