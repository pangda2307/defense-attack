import requests
import time
import random
import threading


def get_public_ip():
    try:
        response = requests.get('https://api.ipify.org?format=json')
        response.raise_for_status()  # 如果请求失败，会抛出异常
        ip_data = response.json()
        return ip_data['ip']
    except requests.RequestException as e:
        print(f"Error occurred: {e}")
        return None


thread_local = threading.local()    

new_boundary=''
def new_file(new_fuben):
    
    # 文件路径
    fuben = '110jingcha_body'#开头文字
    fuben_bo = '110jingcha_body_b'#z中间二进制
    fuben_zh = '110jingcha_body_z'#z结尾文字
    random_number_1 = random.randint(1000, 9999)
    random_number_2 = random.randint(1000, 9999)
    random_number_3 = random.randint(1000, 9999)
    random_number_4 = random.randint(1000, 9999)
    random_number_5 = random.randint(10, 99)
    thread_local.new_boundary = f'314f{random_number_1}-{random_number_2}-435c-{random_number_3}-{random_number_4}e30c4f{random_number_5}'
    new_img_name = f'IMG_20240445_193649_{random_number_4}{random_number_5}.jpg'

    neirong=[]
    # 读取文件内容
    with open(fuben, 'r',encoding='utf-8') as file:
        sub_neirong = file.read()
        neirong.append(sub_neirong)

    with open(fuben_bo, 'rb') as file:
        sub_neirong = file.read()
        neirong.append(sub_neirong)

    with open(fuben_zh, 'r') as file:
        sub_neirong = file.read()
        neirong.append(sub_neirong)

    # 替换boundary值
    neirong[0] = ''.join(neirong[0]).replace('314f7088-8923-435c-9391-2071e30c4f28', new_boundary)
    neirong[0] = ''.join(neirong[0]).replace('IMG_20240445_193649.jpg', new_img_name)
    neirong[2] = ''.join(neirong[2]).replace('314f7088-8923-435c-9391-2071e30c4f28', new_boundary)

    # 将修改后的内容写入新文件
    
    with open(new_fuben, 'a') as file:
        data=''.join(neirong[0])
        file.write(data)


    with open(new_fuben, 'ab') as file:
        data=neirong[1]
        file.write(data)

    with open(new_fuben, 'a') as file:
        data=''.join(neirong[2])
        file.write(data)

    return new_fuben


def up_load(file_path):
    # 文件路径
    


    # 请求的URL
    url = 'http://120.24.184.219:16890/api/uploadImgs'

    # 设置请求头
    headers = {
        #'Content-Type': 'multipart/form-data; boundary=314f7088-8923-435c-9391-2071e30c4f27',
        #'Content-Length': '5330178',  # Content-Length 通常由 requests 自动处理
        'Content-Type': f'multipart/form-data; boundary={new_boundary}',
        'Host': '120.24.184.219:16890',
        'Connection': 'Keep-Alive',
        'Accept-Encoding': 'gzip',
        'User-Agent': 'okhttp/4.10.0'
    }




    #first_ip = get_public_ip()
    #print(first_ip)
    # 上传文件
    with open(file_path, 'rb') as file:
        files = {'file': file}
        
        # 发起请求
    
        response = requests.post(url, files=files, headers=headers) 

        # 打印响应状态码和响应体
        print(f"Status Code: {response.status_code}")
        print(f"Response Text: {response.text}")
        '''if first_ip != get_public_ip():
            print("IP has changed, restarting upload...")
        # 检查是否为JSON格式的响应'''
        try:
            response_json = response.json()
            print(f"Response JSON: {response_json}")
        except ValueError:
            print("Response is not in JSON format.")
        time.sleep(0.2)

def loop_thread(filaname):
    while True:   
        filepath=new_file(filaname)  # 假设这是一个已定义的函数
        up_load(filepath)
        # 每次循环打开 '110jingcha' 文件，并写入空字节
        with open(filepath, 'wb') as file:
            file.write(b'')
        print(f'线程{filaname}正在运行{new_boundary}')
        time.sleep(1)



if __name__ == '__main__':
    for i in range(25):
        threading.Thread(target=loop_thread, args=(f'110jingcha{i}',)).start()
        '''threading.Thread(target=loop_thread, args=('999jingcha',)).start()
        threading.Thread(target=loop_thread, args=('120jingcha',)).start()
        threading.Thread(target=loop_thread, args=('99jingcha',)).start()'''
        