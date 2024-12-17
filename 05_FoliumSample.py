import folium
import requests


# 住所や名称から緯度経度を取得する
def geo_coding(address):
    url = f"https://msearch.gsi.go.jp/address-search/AddressSearch?q={address}"

    res = requests.get(
        url=url
    )
    data = res.json()

    return data[0]['geometry']['coordinates']

if __name__ == "__main__":
    # 掲載する情報一覧
    data_list = [
        {
            "発生場所": "各務原市那加西那加町",
            "詳細": "帰宅中の女子学生に対し、男が車で後をつける事案が発生しました。"
        },
        {
            "発生場所": "恵那市長島町正家",
            "詳細": "帰宅中の児童らに対し、男が手を振ったり、女がスマートフォンを向ける事案が発生しました。"
        },
        {
            "発生場所": "岐阜市中１丁目",
            "詳細": "下校中の児童らに対し、男が携帯電話機を向ける事案が発生しました。"
        },
        {
            "発生場所": "岐阜市中西郷",
            "詳細": "下校中の児童らに対し、男が携帯電話機のカメラを向ける事案が発生しました。"
        },
    ]

    map_object = folium.Map(
        location=[35.4096218, 136.754722],
        zoom_start=12
    )

    for data in data_list:
        location = geo_coding(data["発生場所"])

        folium.Marker(
            location=[location[1], location[0]],
            tooltip=data["詳細"][0:5] + "・・・",
            popup=folium.Popup(data["詳細"], parse_html=True, max_width=100),
            icon=folium.Icon(color="green")
        ).add_to(map_object)

    # 生成したマップを保存する
    map_object.save("sample.html")
