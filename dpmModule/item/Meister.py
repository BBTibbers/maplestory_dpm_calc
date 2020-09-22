from . import ItemKernel as it
ExMDF = it.ExMDF

Ring = it.Item(name="마이스터링", level = 140, main_option = ExMDF(stat_main = 5, stat_sub = 5, att = 1))
Ear = it.Item(name="마이스터 이어링", level = 140, main_option = ExMDF(stat_main = 5, stat_sub = 5, att = 4))
Soulder = it.Item(name="마이스터 숄더", level = 140, main_option = ExMDF(stat_main = 13, stat_sub = 13, att = 9))
Pendant = it.Item(name="마이스터 제작 펜던트", level = 130, main_option = ExMDF(stat_main = 16))
Face = it.Item(name="샤이니 마이스터 제작 심볼", level = 130, main_option = ExMDF(stat_main = 3, att = 3))

class Factory():
    
    @staticmethod
    def getAccesoryDict(nth_ring, star, enhance = True, potential = it.ExMDF(), additional_potential = it.ExMDF(), bonus = it.ExMDF(), hammer = True):
        #Always use 30% enhance scroll. if False, do not apply.
        if not hammer:
            upgrades = [6,1,1]
        else:
            upgrades = [7,2,2]
        
        miester_ring = Ring.copy()
        miester_ear = Ear.copy()
        miester_shoulder = Soulder.copy()
        miester_pendant = Pendant.copy()
        miester_face = Face.copy()
        
        for item, idx in zip([miester_ring, miester_ear, miester_shoulder, miester_pendant, miester_face], [0,1,2,3,4]):
            if idx == 1:
                item.add_main_option(bonus)
            if idx == 3:
                item.add_main_option(bonus)
            if idx == 4:
                item.add_main_option(bonus)

            
            item.set_potential(potential)
            item.set_additional_potential(additional_potential)
            
            if idx < 3 :
                item.add_main_option(it.EnhancerFactory.get_armor_starforce_enhancement(140, star))
            if idx > 2 :      
                item.add_main_option(it.EnhancerFactory.get_armor_starforce_enhancement(130, star))
            
     
            
        
        return {"ring"+str(nth_ring) : miester_ring, "ear" : miester_ear, "shoulder" : miester_shoulder, "pendant" : miester_pendant, "face" : miester_face}