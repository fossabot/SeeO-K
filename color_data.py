# RGB Dictionary
RGB = {
    (0, 0, 255): '차가운 파란색',
    (0, 0, 130): '어두운 남색',
    (255, 150, 0): '밝은 주황색',
    (255, 0, 0): '강렬한 빨간색',
    (255, 0, 200): '화사한 분홍색',
    (0, 255, 0): '생기있는 초록색',
    (255, 255, 255): '흰색',
    (125, 125, 125): '회색',
    (217, 217, 215): '밝은회색',
    (83, 86, 90): '어두운 회색',
    (127, 24, 77): '자주색',
    (218, 64, 97): '라즈베리색',
    (227, 51, 149): '형광분홍색',
    (241, 161, 181): '연한 분홍색',
    (242, 171, 141): '복숭아색',
    (255, 127, 80): '산호색',
    (250, 225, 125): '밝은 노란색',
    (252, 234, 78): '화사한 노란색',
    (241, 179, 62): '귤색',
    (212, 237, 76): '파스텔 연두색',
    (137, 198, 60): '밝은 초록색',
    (87, 193, 172): '상큼한 민트색',
    (122, 133, 60): '올리브색',
    (91, 90, 57): '카키색',
    (27, 66, 33): '어두운 초록색',
    (86, 192, 231): '밝은 하늘색',
    (168, 122, 202): '라벤더색',
    (79, 15, 108): '쨍한 보라색',
    (120, 34, 47): '버건디색',
    (117, 47, 23): '어두운 갈색',
    (162, 115, 38): '겨자색',
    (202, 180, 148): '모래색',
    (192, 208, 224): '연청색',
    (0, 0, 0): '검정색',
    (207, 185, 142):'진한 베이지색',
    (252, 240, 217):'밝은 베이지색',
    (248, 248, 234):'밝은 아이보리색'
}

# RGB 값들을 리스트로 변환
rgb = list(RGB.keys())
rgb_len = len(rgb)


# 옷의 색에서 추출된 RGB 값들(rgb_list)을 위 자료구조에서의 RGB 값들과 비교해 가장 비슷한 색을 추출
def extract_color(rgb_list):
    color_name_list = []
    for i in range(len(rgb_list)):
        minimum = 99999999
        for j in range(rgb_len):
            chai = 0
            # R, G, B 3가지 비교
            for k in range(3):
                chai += abs(rgb_list[i][k] - rgb[j][k])
            if chai < minimum:
                minimum = chai
                closest_color = RGB[rgb[j]]
        color_name_list.append(closest_color)
    return color_name_list
