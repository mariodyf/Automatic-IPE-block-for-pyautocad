from pyautocad import Autocad, aDouble, APoint
acad = Autocad()
print(acad)

#  CONSTANTS dimensions
IPE = {
    # PERFIL,H,B,E1,E2,R
    80: [0.08, 0.046, 0.0038, 0.0052, 0.005],
    100: [0.1, 0.055, 0.0041, 0.0057, 0.007],
    120: [0.12, 0.064, 0.0044, 0.0063, 0.007],
    140: [0.14, 0.073, 0.0047, 0.0069, 0.007],
    160: [0.16, 0.082, 0.005, 0.0074, 0.009],
    180: [0.18, 0.091, 0.0053, 0.008, 0.009],
    200: [0.2, 0.1, 0.0056, 0.0085, 0.012],
    220: [0.22, 0.11, 0.0059, 0.0092, 0.012],
    240: [0.24, 0.12, 0.0062, 0.0098, 0.015],
    270: [0.27, 0.135, 0.0066, 0.0102, 0.015],
    300: [0.3, 0.15, 0.0071, 0.0107, 0.015],
    330: [0.33, 0.16, 0.0075, 0.0115, 0.018],
    360: [0.36, 0.17, 0.008, 0.0127, 0.018],
    400: [0.4, 0.18, 0.0086, 0.0135, 0.021],
    450: [0.45, 0.19, 0.0094, 0.0146, 0.021],
    500: [0.5, 0.2, 0.0102, 0.016, 0.021],
    550: [0.55, 0.21, 0.0111, 0.0172, 0.024],
    600: [0.6, 0.22, 0.012, 0.019, 0.024]
}

HEA = {
    # PERFIL,H,B,E1,E2,R
    100: [0.1, 0.1, 0.005, 0.018, 0.012],
    120: [0.11, 0.12, 0.005, 0.018, 0.012],
    140: [0.13, 0.14, 0.0055, 0.0185, 0.012],
    160: [0.15, 0.16, 0.006, 0.019, 0.015],
    180: [0.17, 0.18, 0.006, 0.0195, 0.015],
    200: [0.19, 0.2, 0.0065, 0.01, 0.018],
    220: [0.21, 0.22, 0.007, 0.011, 0.018],
    240: [0.23, 0.24, 0.0075, 0.012, 0.021],
    260: [0.25, 0.26, 0.0075, 0.0125, 0.024],
    280: [0.27, 0.28, 0.008, 0.013, 0.024],
    300: [0.29, 0.3, 0.0085, 0.014, 0.027],
    320: [0.31, 0.3, 0.009, 0.0155, 0.027],
    340: [0.33, 0.3, 0.0095, 0.0165, 0.027],
    360: [0.35, 0.3, 0.01, 0.0175, 0.027],
    400: [0.39, 0.3, 0.011, 0.019, 0.027],
    450: [0.44, 0.3, 0.0115, 0.021, 0.027],
    500: [0.49, 0.3, 0.012, 0.023, 0.027],
    550: [0.54, 0.3, 0.0125, 0.024, 0.027],
    600: [0.59, 0.3, 0.013, 0.025, 0.027]
}

HEB = {
    # PERFIL,H,B,E1,E2,R
    100: [0.1, 0.1, 0.006, 0.01, 0.012],
    120: [0.12, 0.12, 0.0065, 0.011, 0.012],
    140: [0.14, 0.14, 0.007, 0.012, 0.012],
    160: [0.16, 0.16, 0.008, 0.013, 0.015],
    180: [0.18, 0.18, 0.0085, 0.014, 0.015],
    200: [0.2, 0.2, 0.009, 0.015, 0.018],
    220: [0.22, 0.22, 0.0095, 0.016, 0.018],
    240: [0.24, 0.24, 0.01, 0.017, 0.021],
    260: [0.26, 0.26, 0.01, 0.0175, 0.024],
    280: [0.28, 0.28, 0.0105, 0.018, 0.024],
    300: [0.3, 0.3, 0.011, 0.019, 0.027],
    320: [0.32, 0.3, 0.0115, 0.0205, 0.027],
    340: [0.34, 0.3, 0.012, 0.0215, 0.027],
    360: [0.36, 0.3, 0.0125, 0.0225, 0.027],
    400: [0.4, 0.3, 0.0135, 0.024, 0.027],
    450: [0.45, 0.3, 0.014, 0.026, 0.027],
    500: [0.5, 0.3, 0.0145, 0.028, 0.027],
    550: [0.55, 0.3, 0.015, 0.029, 0.027],
    600: [0.6, 0.3, 0.0155, 0.03, 0.027]
}

HEM = {
    # PERFIL,H,B,E1,E2,R
    100: [0.12, 0.106, 0.012, 0.02, 0.012],
    120: [0.14, 0.126, 0.0125, 0.021, 0.012],
    140: [0.16, 0.146, 0.013, 0.022, 0.012],
    160: [0.18, 0.166, 0.014, 0.023, 0.015],
    180: [0.2, 0.186, 0.0145, 0.024, 0.015],
    200: [0.22, 0.206, 0.015, 0.025, 0.018],
    220: [0.24, 0.226, 0.0155, 0.026, 0.018],
    240: [0.27, 0.248, 0.018, 0.032, 0.021],
    260: [0.29, 0.268, 0.018, 0.0325, 0.024],
    280: [0.31, 0.288, 0.0185, 0.033, 0.024],
    300: [0.34, 0.31, 0.021, 0.039, 0.027],
    320: [0.36, 0.309, 0.021, 0.04, 0.027],
    340: [0.38, 0.309, 0.021, 0.04, 0.027],
    360: [0.4, 0.308, 0.021, 0.04, 0.027],
    400: [0.43, 0.307, 0.021, 0.04, 0.027],
    450: [0.48, 0.307, 0.021, 0.04, 0.027],
    500: [0.52, 0.306, 0.021, 0.04, 0.027],
    550: [0.57, 0.306, 0.021, 0.04, 0.027],
    600: [0.62, 0.305, 0.021, 0.04, 0.027]
}
def build_draw_params_IPE_HE(family, height): # constucción de IPE y HEA, HEB, HEM
    """ Creates points, and bulges parameters """
    h,b,e1,e2,r = family[height]   # variables perfil seleccionado
    points = [         # puntos del perfil
        0, 0, 0,
        0, e2, 0,
        ((b/2)-(e1/2)-r), e2, 0,
        ((b/2)-(e1/2)), e2+r, 0,
        ((b/2)-(e1/2)), (h-e2)-r, 0,
        ((b/2)-(e1/2)-r), (h-e2), 0,
        0, (h-e2), 0,
        0, h, 0,
        b, h, 0,
        b, (h-e2), 0,
        ((b/2)+(e1/2)+r), (h-e2), 0,
        ((b/2)+(e1/2)), (h-e2-r), 0,
        ((b/2)+(e1/2)), e2+r, 0,
        ((b/2)+(e1/2)+r), e2, 0,
        b, e2, 0,
        b, 0, 0,
        0, 0, 0,
    ]
    bulge_value = 2**0.5-1    # (square root of 2)-1
    bulge_params = [        # segment number, bulge value
        (2, bulge_value),
        (4, bulge_value),
        (10, bulge_value),
        (12, bulge_value)
    ]
    return points,bulge_params

def define_block(insertion, name):
    acad.doc.Blocks.Add(APoint(*insertion), name)
    block = acad.doc.Blocks.Item(name)
    return block

def draw_block(block, points, arcs):
    p = aDouble(points)
    pl = block.AddPolyline(p)
    for a in arcs:
        pl.SetBulge(*a)
    pl.Update()
    return pl

def get_family():
    """Get and validate beam family from user"""
    families = {'1': IPE, '2': HEA, '3': HEB, '4': HEM}
    family_names = { '1': 'IPE', '2': 'HEA', '3': 'HEB', '4': 'HEM'}
    print("Elige la familia de perfil:\n1. IPE\n2. HEA\n3. HEB\n4. HEM")
    while True:
        choice = input("Introduce el número de la familia: ")
        if choice in families:
            return families[choice], family_names[choice]
        else:
            print("Error, introduce un número válido")
            
def get_profile_size():
    family, family_name = get_family()
    """Get and validate beam size from user"""
    print("Elige el perfil: ", end='')
    while True:
        try:
            profile_height = int(input("Canto de perfil en mm:"))
            if profile_height not in family:
                raise ValueError
            break
        except ValueError:
            print("Error, introduce un número válido")
    return family, family_name, profile_height

def main():
    family, family_name, profile_height = get_profile_size()
    block_name = f"{family_name}_{profile_height}"

    acad.ActiveDocument.ActiveLayer = acad.doc.Layers.Item("0")
    p_points, p_arcs  = build_draw_params_IPE_HE(family, profile_height)
    block = define_block(p_points[:2], block_name)
    _ = draw_block(block, p_points, p_arcs)
    block_ref = acad.model.InsertBlock(APoint(*p_points[:2]), block_name, 1, 1, 1, 0)

    try:
        # get bounding box
        min_pt, max_pt = block_ref.GetBoundingBox()

        # convert to APoint (ensure 3D)
        min_ap = APoint(min_pt[0], min_pt[1], min_pt[2] if len(min_pt) > 2 else 0)
        max_ap = APoint(max_pt[0], max_pt[1], max_pt[2] if len(max_pt) > 2 else 0)

        # ZoomWindow expects APoint objects
        acad.app.ZoomWindow(min_ap, max_ap)

    except Exception as e:
        print("Zoom failed:", e)
        print(f"Block {block_name} inserted. Programa finalizado con éxito")

if __name__ == '__main__':
    main()
