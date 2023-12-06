import streamlit as st
import pandas as pd
import plotly.express as px

# Excelファイルを読み込む

@st.cache
def load_data():
    df = pd.read_excel("questionnaire.xlsx")
    return df

def calculate_avg_score(factor_data):
    total_score = 0
    for idx, row in factor_data.iterrows():
        st.markdown(f"**{row['設問名']}**")
        score = st.radio("回答", options1, key=row["設問名"])
        if not pd.isna(row["反転"]):
            score = 5 - int(score[0])
        else:
            score = int(score[0])
        total_score += score
    return total_score / len(factor_data)


df = load_data()
# 設問を表示
st.title("ストレスチェックアプリ")
st.caption("Created by 72回生　理数科情報班")

# ラジオボタンのデフォルト選択肢
options1 = ["1 全くあてはまらない", "2 あまりあてはまらない", "3 少しあてはまる", "4 とてもあてはまる"]

# ラジオボタンで回答を収集し、因子ごとの平均点を計算
factor_scores = {}
for factor, factor_data in df.groupby("因子名"):
    st.subheader(factor)
    avg_score = calculate_avg_score(factor_data)
    factor_scores[factor] = avg_score
    st.write(f"{factor}の平均点: {avg_score:.2f}")

# 3つの因子F1～F3の平均値を変数に格納
avg_score_f1 = factor_scores.get("F1", 0)
avg_score_f2 = factor_scores.get("F2", 0)
avg_score_f3 = factor_scores.get("F3", 0)

# レーダーチャートを描画
if factor_scores:
    st.subheader("因子ごとの評価")
    fig = px.line_polar(
        r=list(factor_scores.values()),
        theta=list(factor_scores.keys()),
        line_close=True
    )
    fig.update_layout(font=dict(size=20))

    # レーダーチャートの半径を固定
    fig.update_layout(
        polar=dict(
            radialaxis=dict(
                range=[0, 4]  # 半径の範囲を指定
            )
        ),
        font=dict(size=20)
    )

    st.plotly_chart(fig)

if avg_score_f1 < 2.5 :
    st.write("aaa")
    else:
    st.write("ddd")

if avg_score_f2 < 2.5 :
    st.write("bbb")
    else:
    st.write("eee")

if avg_score_f3 < 2.5 :
    st.write("CCC")
    else:
    st.write("fff")

