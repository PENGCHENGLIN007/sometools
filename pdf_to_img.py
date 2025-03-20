import os

import fitz
from pymupdf import Pixmap


def output_pdf(des_path, dst_img_path):
    a4_width, a4_height = 595, 842  # A4纸的点数尺寸
    pdf_doc = fitz.open()
    imgs = os.listdir(dst_img_path)
    imgs.sort()

    for img_path in imgs:
        img_pixmap = Pixmap(os.path.join(dst_img_path, img_path))
        # 将图片插入PDF文档
        page = pdf_doc.new_page(width=a4_width, height=a4_height)
        page.insert_image(page.rect, pixmap=img_pixmap)
    pdf_doc.save(des_path)
    pdf_doc.close()
    pass

def export_img(ori_path,src_img_path):
    pdf_document = fitz.open(ori_path)
    for page_num in range(pdf_document.page_count):
        page = pdf_document[page_num]
        img = page.get_pixmap(dpi=150, alpha=False)
        #img = page.get_pixmap(alpha=False)
        img.save(f'{src_img_path}/{page_num}.png')


if __name__ == '__main__':
    ori_path = r'xxx.pdf'
    src_img_path = r'xxx\img'
    export_img(ori_path, src_img_path)