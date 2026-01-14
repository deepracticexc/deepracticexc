#!/usr/bin/env python3
"""
代理IP服务测试脚本
测试代理的连接性、功能性和IP地址
"""

import requests
import time
from datetime import datetime

# 代理配置
PROXY_HOST = "202.160.87.48"
PROXY_PORT = "46322"
PROXY_USER = "7A2JxRA2021608748A46322"
PROXY_PASS = "AE39kqdcw7UZ"

# 构建代理URL
proxy_url = f"http://{PROXY_USER}:{PROXY_PASS}@{PROXY_HOST}:{PROXY_PORT}"

proxies = {
    'http': proxy_url,
    'https': proxy_url
}

def print_header(text):
    """打印格式化的标题"""
    print("\n" + "=" * 60)
    print(f"  {text}")
    print("=" * 60)

def test_proxy_connection():
    """测试代理连接性"""
    print_header("测试 1: 代理连接性测试")

    try:
        print(f"代理地址: {PROXY_HOST}:{PROXY_PORT}")
        print(f"用户名: {PROXY_USER}")
        print(f"正在测试连接...")

        start_time = time.time()
        response = requests.get(
            'http://httpbin.org/ip',
            proxies=proxies,
            timeout=30
        )
        elapsed_time = time.time() - start_time

        if response.status_code == 200:
            print(f"✓ 连接成功!")
            print(f"  响应时间: {elapsed_time:.2f} 秒")
            print(f"  返回的IP地址: {response.json()['origin']}")
            return True
        else:
            print(f"✗ 连接失败，状态码: {response.status_code}")
            return False

    except requests.exceptions.ProxyError as e:
        print(f"✗ 代理错误: {e}")
        return False
    except requests.exceptions.Timeout as e:
        print(f"✗ 连接超时: {e}")
        return False
    except Exception as e:
        print(f"✗ 发生错误: {e}")
        return False

def test_https_support():
    """测试HTTPS支持"""
    print_header("测试 2: HTTPS 支持测试")

    try:
        print("正在测试HTTPS连接...")

        start_time = time.time()
        response = requests.get(
            'https://httpbin.org/ip',
            proxies=proxies,
            timeout=30,
            verify=True
        )
        elapsed_time = time.time() - start_time

        if response.status_code == 200:
            print(f"✓ HTTPS连接成功!")
            print(f"  响应时间: {elapsed_time:.2f} 秒")
            print(f"  返回的IP地址: {response.json()['origin']}")
            return True
        else:
            print(f"✗ HTTPS连接失败，状态码: {response.status_code}")
            return False

    except Exception as e:
        print(f"✗ HTTPS测试失败: {e}")
        return False

def test_geo_location():
    """测试代理IP的地理位置"""
    print_header("测试 3: IP地理位置查询")

    try:
        print("正在查询IP地理位置...")

        # 使用ipapi.co获取地理位置信息
        response = requests.get(
            'https://ipapi.co/json/',
            proxies=proxies,
            timeout=30
        )

        if response.status_code == 200:
            data = response.json()
            print(f"✓ 地理位置信息:")
            print(f"  IP地址: {data.get('ip', 'N/A')}")
            print(f"  国家: {data.get('country_name', 'N/A')} ({data.get('country_code', 'N/A')})")
            print(f"  城市: {data.get('city', 'N/A')}")
            print(f"  地区: {data.get('region', 'N/A')}")
            print(f"  ISP: {data.get('org', 'N/A')}")
            print(f"  时区: {data.get('timezone', 'N/A')}")
            return True
        else:
            print(f"✗ 地理位置查询失败，状态码: {response.status_code}")
            return False

    except Exception as e:
        print(f"✗ 地理位置查询失败: {e}")
        return False

def test_response_headers():
    """测试HTTP响应头"""
    print_header("测试 4: HTTP响应头测试")

    try:
        print("正在获取响应头信息...")

        response = requests.get(
            'http://httpbin.org/headers',
            proxies=proxies,
            timeout=30
        )

        if response.status_code == 200:
            headers = response.json()['headers']
            print(f"✓ 响应头信息:")
            print(f"  User-Agent: {headers.get('User-Agent', 'N/A')}")
            print(f"  X-Forwarded-For: {headers.get('X-Forwarded-For', 'N/A')}")
            return True
        else:
            print(f"✗ 获取响应头失败，状态码: {response.status_code}")
            return False

    except Exception as e:
        print(f"✗ 响应头测试失败: {e}")
        return False

def test_speed():
    """测试代理速度"""
    print_header("测试 5: 代理速度测试")

    try:
        print("正在进行速度测试（下载小文件）...")

        # 测试下载一个小文件
        start_time = time.time()
        response = requests.get(
            'http://httpbin.org/bytes/102400',  # 下载100KB数据
            proxies=proxies,
            timeout=30
        )
        elapsed_time = time.time() - start_time

        if response.status_code == 200:
            data_size = len(response.content) / 1024  # KB
            speed = data_size / elapsed_time  # KB/s
            print(f"✓ 速度测试完成:")
            print(f"  下载大小: {data_size:.2f} KB")
            print(f"  耗时: {elapsed_time:.2f} 秒")
            print(f"  速度: {speed:.2f} KB/s")
            return True
        else:
            print(f"✗ 速度测试失败，状态码: {response.status_code}")
            return False

    except Exception as e:
        print(f"✗ 速度测试失败: {e}")
        return False

def main():
    """主函数"""
    print("\n" + "🔍 代理IP服务测试工具" + "\n")
    print(f"测试时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"代理服务器: {PROXY_HOST}:{PROXY_PORT}")

    # 执行所有测试
    results = {
        "连接性测试": test_proxy_connection(),
        "HTTPS支持": test_https_support(),
        "地理位置": test_geo_location(),
        "响应头测试": test_response_headers(),
        "速度测试": test_speed()
    }

    # 总结测试结果
    print_header("测试结果总结")

    passed = sum(results.values())
    total = len(results)

    for test_name, result in results.items():
        status = "✓ 通过" if result else "✗ 失败"
        print(f"{test_name}: {status}")

    print(f"\n总计: {passed}/{total} 项测试通过")

    if passed == total:
        print("\n🎉 代理服务完全正常！")
    elif passed > 0:
        print("\n⚠️  代理服务部分功能正常")
    else:
        print("\n❌ 代理服务无法使用")

if __name__ == "__main__":
    main()
