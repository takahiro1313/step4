from fastapi import FastAPI, HTTPException, Body, Depends
from starlette.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import pymysql
import os
from datetime import datetime
from dotenv import load_dotenv
from typing import List
#dbあきらめ
# import sqlite3

app = FastAPI()


# CORSを回避するために追加
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,   # 追記により追加
    allow_methods=["*"],      # 追記により追加
    allow_headers=["*"]       # 追記により追加
)

# .envファイルを読み込む
load_dotenv()


class ProductQuery(BaseModel):
    code: str


@app.get("/")
def read_root():
    return {"おはよう": "おやすみ"}


drink = {
    "PRD_ID":"001",
    "PRD_CD": "4902220772414",
    "PRD_NAME": "クリアアサヒ",
    "PRD_PRICE": "178"
    }

# test用
@app.post("/search_product/")
def search_product(product_query: ProductQuery = Body(...)):
    print(f"Received code: {product_query.code}")
    if product_query.code == drink["PRD_CD"]:
        return {
            "status": "success",
            "message": drink
            }
    else:
        return{
            "status": "failed"
        }











# class ProductQuery(BaseModel):
#     code: str

# SQLiteデータベースに接続
# conn = sqlite3.connect('./db_product.db')
# c = conn.cursor()

# class Product(BaseModel):
#     PRD_ID: str
#     PRD_CD: str
#     PRD_NAME: str
#     PRD_PRICE: int


# # 商品情報を取得するAPIエンドポイント
# # @app.post('/search_product', methods=['POST'])
# # def search_product():
# @app.post("/search_product/")
# async def search_product(product_query: Product):
#     # product_query = request.json
#     print(f"Received code: {product_query['code']}")

#     # SQLiteデータベースから商品情報を取得
#     c.execute("SELECT * FROM products WHERE PRD_CD = ?", (product_query.PRD_CD,))
#     result = c.fetchone()

#     if result:
#         product = {
#             "PRD_ID": result[0],
#                 "PRD_CD": result[1],
#                 "PRD_NAME": result[2],
#                 "PRD_PRICE": result[3]
#         }
#         return product
#     else:
#              raise HTTPException(status_code=404, detail="Product not found")
#         )

# if __name__ == '__main__':
#     app.run(debug=True)
