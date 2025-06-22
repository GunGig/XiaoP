# XiaoP/api_services/api_handler.py

import requests
import json

def get_random_joke():
    """
    从一个公共API获取一个随机的英文笑话。
    (此函数未作改动)
    """
    joke_api_url = "https://official-joke-api.appspot.com/random_joke"

    try:
        response = requests.get(joke_api_url, timeout=5)
        if response.status_code == 200:
            joke_data = response.json()
            setup = joke_data.get("setup", "好像没找到笑话的铺垫...")
            punchline = joke_data.get("punchline", "emmm...笑点跑掉了！")
            return f"{setup}\n... {punchline} 😄"
        else:
            return f"获取笑话失败了，网络服务员说错误码是：{response.status_code}"
    except requests.exceptions.RequestException as e:
        return f"网络连接出错了！无法联系到笑话中心。错误信息：{e}"

def get_amap_weather(city_adcode):
    """
    (高德天气API版 - 已修复并优化)
    根据城市编码(adcode)从高德开放平台获取实时天气。
    此函数特别处理了无效adcode会导致API返回一个包含空列表的特殊情况。
    """
    api_key = 'd0efe2e3026aea2fa8e3e369b7e6255d'

    if not city_adcode:
        return "我需要一个有效的城市编码才能查询天气。"

    weather_url = f"https://restapi.amap.com/v3/weather/weatherInfo?city={city_adcode}&key={api_key}&extensions=base"

    try:
        response = requests.get(weather_url, timeout=5)

        if response.status_code == 200:
            weather_data = response.json()

            if weather_data.get('status') == '1':
                live_weather_list = weather_data.get('lives')

                # --- 这是最终、最稳健的检查逻辑 ---
                # 1. 'lives' 键存在且其值为列表。
                # 2. 该列表不为空。
                # 3. 列表的第一个元素是字典（而不是另一个列表）。
                # 4. 该字典不为空。
                if (isinstance(live_weather_list, list) and
                        len(live_weather_list) > 0 and
                        isinstance(live_weather_list[0], dict) and
                        live_weather_list[0]):

                    live_weather = live_weather_list[0]

                    city = live_weather.get('city', '未知城市')
                    weather = live_weather.get('weather', '未知')
                    temperature = live_weather.get('temperature', '未知')
                    wind_direction = live_weather.get('winddirection', '未知')
                    wind_power = live_weather.get('windpower', '未知')
                    humidity = live_weather.get('humidity', '未知')
                    report_time = live_weather.get('reporttime', '未知时间')

                    return (
                        f"{city}的实时天气：{weather}，"
                        f"温度：{temperature}°C，"
                        f"{wind_direction}风 {wind_power}级，"
                        f"空气湿度：{humidity}%。 "
                        f"(数据更新于: {report_time})"
                    )
                else:
                    # 这个 'else' 分支现在可以正确地捕获 'status' 为 '1'
                    # 但 'lives' 中数据无效的情况，这种情况通常意味着 adcode 错误。
                    return f"发送的城市编码 '{city_adcode}' 有误，无法找到对应的天气信息。"
            else:
                error_info = weather_data.get('info', '未知错误')
                return f"天气服务返回错误：{error_info}"
        else:
            return f"连接天气服务器失败，服务器返回错误码：{response.status_code}"

    except requests.exceptions.RequestException as e:
        return f"网络连接出错了！无法获取天气信息。错误详情：{e}"



# --- 主程序入口和测试区 ---
if __name__ == '__main__':
    print("--- 开始测试 api_handler.py 模块 (最终修复版) ---")

    print("\n[测试] 正在获取北京的天气 (正确编码)...")
    beijing_adcode = "110000"
    weather_report = get_amap_weather(beijing_adcode)
    print(f"小P对北京天气的回复：\n{weather_report}")

    print("\n[测试] 正在尝试一个错误的城市编码...")
    invalid_report = get_amap_weather("999999")
    print(f"小P对错误编码的回复：\n{invalid_report}")

    print("\n" + "=" * 30 + "\n")

    print("[测试] 正在为你获取一个随机笑话...")
    joke = get_random_joke()
    print(joke)

    print("\n--- API模块测试结束 ---")