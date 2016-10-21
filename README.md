# idlimit
自动给身份证或营业执照添加“仅供xxx使用——“

安装方法：

    mkdir -p ~/projects
    cd ~/projects
    git clone https://github.com/zhangriyueming/idlimit.git
    chmod +x ~/projects/idlimit/sfz.py
    ln -s ~/projects/idlimit/sfz.py /usr/local/bin/sfz

将身份证正面照片保存到 ~/projects/idlimit/sfz_front.jpg

将身份证背面照片保存到 ~/projects/idlimit/sfz_back.jpg

使用方法：

若要生成 “仅供明日科技使用——” 的图片，在命令行中输入：

    sfz 明日科技

