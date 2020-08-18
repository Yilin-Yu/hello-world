# 下载GRE词汇MP3文件到本地
import os
import requests

def DownloadFile(mp3_url, save_url,file_name):
    try:
        if mp3_url is None or save_url is None or file_name is None:
            print('参数错误')
            return None
        # 文件夹不存在，则创建文件夹
        folder = os.path.exists(save_url)
        if not folder:
            os.makedirs(save_url)
        # 读取MP3资源
        res = requests.get(mp3_url,stream=True)
        # 获取文件地址
        file_path = os.path.join(save_url, file_name)
        print('开始写入文件：', file_path)
        # 打开本地文件夹路径file_path，以二进制流方式写入，保存到本地
        with open(file_path, 'wb') as fd:
            for chunk in res.iter_content():
                fd.write(chunk)
        print(file_name+' 成功下载！')
    except:
        print("程序错误")

def DownloadMP3(i_li):
    # MP3源地址url
    url = 'http://download.dogwood.com.cn/online/ynm3000bx/%s.mp3' % (i_li)
    # MP3保存文件夹
    save_url='D:/GRE/'
    # MP3文件名
    file_name = '%s.mp3' % (i_li)
    DownloadFile(url,save_url, file_name)
    
if __name__ == "__main__":
    li = []
    for i in range(1, 32):
        li.append(str(("{:0>2d}".format(i))))
    
    for i in li:
        DownloadMP3(i)