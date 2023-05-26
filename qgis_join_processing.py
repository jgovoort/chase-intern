for y in [2019,2020] :
    for i in range(1,5) :
        input = 'D:\\GitHub\\chase-intern\\SON_%i_%i_3031.gpkg|layername=SON_%i_%i_3031'%(i,y,i,y)
        print(input)
        processing.run("native:joinattributesbylocation", {'INPUT': input,'PREDICATE':[4,5,6],'JOIN':'E:/PYYYYYTon/grille.gpkg|layername=grille',
        'JOIN_FIELDS':[],'METHOD':0,'DISCARD_NONMATCHING':False,'PREFIX':'','OUTPUT':'D:/GitHub/chase-intern/GRILLE/SON_%i_%i_GRILLE.csv'%(i,y)})