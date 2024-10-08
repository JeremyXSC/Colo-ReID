# import cv2
import os


def walkFile(file):
    i = 1
    for files in sorted(os.listdir(file)):
        if i % 2 == 0:
            print(files, int(i / 2))
            id = str(format(int(i / 2), "04"))
            os.rename(file + files, file + id + '_c2.mp4')
        else:
            print(files, int(i / 2) + 1)
            id = str(format(int(i / 2) + 1, "04"))
            os.rename(file + files, file + id + '_c1.mp4')
        i += 1


if __name__ == '__main__':
    walkFile('/home/chenqingzhong/data/chenqingzhong/Data/zhongshan_endoscope/polyp_match/polyp_reid/')

    # 模仿DukeMTMC行人重识别数据集重命名息肉数据集的对应关系（如原文件名ch_1_1_0377_0380.mp4和ch_2_1_0377_0380.mp4分别改成0001_c1.mp4和0001_c2.mp4）
    # 注意！！注意！！按命名排序的顺序和自己预想的不同，括号内的编号为修正后的。
    # 最后是通过手动重命名来确保无误。

    # ch_1_1_0377_0380.mp4
    # 1
    # ch_2_1_0377_0380.mp4
    # 1
    # cxy_1_1_0528_0535.mp4
    # 2
    # cxy_2_1_0334_0336.mp4
    # 2
    # gjh_1_2_0309_0313.mp4
    # 3
    # gjh_1_4_0383_0390.mp4
    # 3(4)
    # gjh_2_2_0192_0202.mp4
    # 4(3)
    # gjh_2_4_0247_0250.mp4
    # 4
    # hdr_1_1_0219_0230.mp4
    # 5
    # hdr_2_1_0150_0168.mp4
    # 5
    # hfq_1_1_0310_0318.mp4
    # 6
    # hfq_2_1_0233_0236.mp4
    # 7(6)
    # hfq_1_2_0331_0333.mp4
    # 6(7)
    # hfq_2_2_0245_0248.mp4
    # 7
    # hlb_1_1_0084_0091.mp4
    # 8
    # hlb_2_1_0141_0144.mp4
    # 8
    # lbl_1_3_0167_0169.mp4
    # 9
    # lbl_2_3_0428_0443.mp4
    # 9
    # mqz_1_1_0085_0093.mp4
    # 10
    # mqz_2_1_0022_0031.mp4
    # 10
    # mwl_1_1_0149_0152.mp4
    # 11
    # mwl_1_2_0171_0173.mp4
    # 11(12)
    # mwl_1_3_0216_0222.mp4
    # 12(13)
    # mwl_2_1_0000_0005.mp4
    # 12(11)
    # mwl_2_2_0018_0023.mp4
    # 13(12)
    # mwl_2_3_0063_0068.mp4
    # 13
    # plh_1_1_0143_0146.mp4
    # 14
    # plh_1_2_0177_0183.mp4
    # 14(15)
    # plh_1_3_0310_0314.mp4
    # 15(16)
    # plh_2_1_0173_0178.mp4
    # 15(14)
    # plh_2_2_0209_0211.mp4
    # 16(15)
    # plh_2_3_0292_0296.mp4
    # 16
    # qfj_1_2_0753_0782.mp4
    # 17
    # qfj_2_2_1069_1073.mp4
    # 17
    # qzb_1_1_0305_0308.mp4
    # 18
    # qzb_1_2_0316_0319.mp4
    # 18(19)
    # qzb_2_1_0213_0216.mp4
    # 19(18)
    # qzb_2_2_0227_0229.mp4
    # 19
    # sxx_1_1_0193_0208.mp4
    # 20
    # sxx_2_1_0431_0433.mp4
    # 20
    # tsp_1_1_0138_0142.mp4
    # 21
    # tsp_2_1_0059_0062.mp4
    # 21
    # wdm_1_1_0503_0530.mp4
    # 22
    # wdm_2_1_0165_0170.mp4
    # 22
    # xjf_1_1_0252_0263.mp4
    # 23
    # xjf_2_1_0279_0289.mp4
    # 23
    # xmh_1_1_0260_0297.mp4
    # 24
    # xmh_2_1_0156_0162.mp4
    # 24
    # xxy_1_1_0533_0537.mp4
    # 25
    # xxy_2_1_0359_0361.mp4
    # 25
    # yaz_1_1_0120_0122.mp4
    # 26
    # yaz_1_2_0179_0180.mp4
    # 26(27)
    # yaz_2_1_0223_0225.mp4
    # 27(26)
    # yaz_2_2_0291_0292.mp4
    # 27
    # ybs_1_1_0153_0160.mp4
    # 28
    # ybs_2_1_0535_0543.mp4
    # 28
    # ykf_1_1_0508_0509.mp4
    # 29
    # ykf_2_1_0227_0228.mp4
    # 29
    # zsh_1_1_0160_0170.mp4
    # 30
    # zsh_1_2_0222_0224.mp4
    # 30(31)
    # zsh_2_1_0071_0074.mp4
    # 31(30)
    # zsh_2_2_0107_0112.mp4
    # 31