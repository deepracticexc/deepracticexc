#!/usr/bin/env python3
"""
快速代理连接测试
"""

import socket
import sys

def test_tcp_connection(host, port, timeout=5):
    """测试TCP连接"""
    print(f"正在测试TCP连接到 {host}:{port}...")

    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(timeout)

        result = sock.connect_ex((host, int(port)))
        sock.close()

        if result == 0:
            print(f"✓ TCP连接成功！端口 {port} 是开放的")
            return True
        else:
            print(f"✗ TCP连接失败，端口 {port} 无法连接（错误代码: {result}）")
            return False

    except socket.timeout:
        print(f"✗ 连接超时")
        return False
    except socket.gaierror as e:
        print(f"✗ 域名解析失败: {e}")
        return False
    except Exception as e:
        print(f"✗ 连接错误: {e}")
        return False

if __name__ == "__main__":
    PROXY_HOST = "202.160.87.48"
    PROXY_PORT = "46322"

    print("\n🔍 快速代理TCP连接测试")
    print(f"目标: {PROXY_HOST}:{PROXY_PORT}\n")

    result = test_tcp_connection(PROXY_HOST, PROXY_PORT, timeout=10)

    if result:
        print("\n结论: 代理服务器端口可达，但可能需要进一步测试HTTP/HTTPS功能")
    else:
        print("\n结论: 代理服务器不可达，可能的原因：")
        print("  1. 代理服务器已关闭")
        print("  2. IP地址或端口错误")
        print("  3. 被防火墙阻止")
        print("  4. 网络连接问题")
