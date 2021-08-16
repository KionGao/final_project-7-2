import pygame
import os
from pygame import mixer  #輸入音樂，若有bug將進行修改

mixer.music.load('music','Choosing_sound.wav')
mixer.music.play(-1)

gov_problem = [pygame.image.load(os.path.join("event/gov_img", "Q1.png")),
                pygame.image.load(os.path.join("event/gov_img", "Q2.png")),
                pygame.image.load(os.path.join("event/gov_img", "Q3.png")),
                pygame.image.load(os.path.join("event/gov_img", "Q4.png")),
                pygame.image.load(os.path.join("event/gov_img", "Q5.png"))]

gov_decision_problem1 = [pygame.image.load(os.path.join("event/gov_img", "Q1_A.png")),
                        pygame.image.load(os.path.join("event/gov_img", "Q1_B.png")),
                        pygame.image.load(os.path.join("event/gov_img", "Q1_C.png")),
                        pygame.image.load(os.path.join("event/gov_img", "M1_A.png")),
                        pygame.image.load(os.path.join("event/gov_img", "M1_B.png")),
                        pygame.image.load(os.path.join("event/gov_img", "M1_C.png"))]
gov_impact_problem1 = [[10,0,3,1,3,1],[30,20,1,-1,2,0],[20,10,-1,-3,5,3]]                        
gov_decision_problem2 = [pygame.image.load(os.path.join("event/gov_img", "Q2_A.png")),
                        pygame.image.load(os.path.join("event/gov_img", "Q2_B.png")),
                        pygame.image.load(os.path.join("event/gov_img", "Q2_C.png")),
                        pygame.image.load(os.path.join("event/gov_img", "M2_A.png")),
                        pygame.image.load(os.path.join("event/gov_img", "M2_B.png")),
                        pygame.image.load(os.path.join("event/gov_img", "M2_C.png"))]
gov_impact_problem2 = [[20,10,-1,-3,5,3],[10,0,1,-1,2,0], [30,20,-1,-3,5,3]]
gov_decision_problem3 = [pygame.image.load(os.path.join("event/gov_img", "Q3_A.png")),
                        pygame.image.load(os.path.join("event/gov_img", "Q3_B.png")),
                        pygame.image.load(os.path.join("event/gov_img", "Q3_C.png")),
                        pygame.image.load(os.path.join("event/gov_img", "M3_A.png")),
                        pygame.image.load(os.path.join("event/gov_img", "M3_B.png")),
                        pygame.image.load(os.path.join("event/gov_img", "M3_C.png"))]
gov_impact_problem3 = [[20,10,1,-1,3,1],[10,0,-1,-3,2,0], [10,0,2,0,5,3]]
gov_decision_problem4 = [pygame.image.load(os.path.join("event/gov_img", "Q4_A.png")),
                        pygame.image.load(os.path.join("event/gov_img", "Q4_B.png")),
                        pygame.image.load(os.path.join("event/gov_img", "Q4_C.png")),
                        pygame.image.load(os.path.join("event/gov_img", "M4_A.png")),
                        pygame.image.load(os.path.join("event/gov_img", "M4_B.png")),
                        pygame.image.load(os.path.join("event/gov_img", "M4_C.png"))]
gov_impact_problem4 =[[10,0,3,1,3,1],[30,0,3,-3,5,0], [30,20,-1,-3,2,0]]
gov_decision_problem5 = [pygame.image.load(os.path.join("event/gov_img", "Q5_A.png")),
                        pygame.image.load(os.path.join("event/gov_img", "Q5_B.png")),
                        pygame.image.load(os.path.join("event/gov_img", "Q5_C.png")),
                        pygame.image.load(os.path.join("event/gov_img", "M5_A.png")),
                        pygame.image.load(os.path.join("event/gov_img", "M5_B.png")),
                        pygame.image.load(os.path.join("event/gov_img", "M5_C.png"))]
gov_impact_problem5 =[[10,0,1,-1,2,0],[30,20,-1,-3,2,0], [10,0,-1,-3,5,3]]

gov_decision = [gov_decision_problem1,gov_decision_problem2,gov_decision_problem3,gov_decision_problem4,gov_decision_problem5]
gov_impact = [gov_impact_problem1,gov_impact_problem2,gov_impact_problem3,gov_impact_problem4,gov_impact_problem5]

'''
gov_problem = ['Q：國外爆發delta病毒，要怎麼處理呢','Q：某科技大廠出現確診…但疫調困難足跡還沒確定','Q：施打公費疫苗需要撥多少補助給醫療院所','Q：國內疫情每日只有20人確診 到底要不要解封呢','Q：疫調結果與現況出現嚴重落差']
gov_decision_problem1 = ['A買爆疫苗，但半年後才會到','B大力投資國產疫苗','C限制非本國籍人士進入']
gov_impact_problem1 = [[10,0,5,3,4,2],[50,30,4,2,2,0],[40,20,2,0,4,2]]
gov_decision_problem2 = ['A暫緩公布此案例，避免大眾恐慌','B據實於疫情記者會上公布，但由於隱私問題，不主動公布確診者公司','C為了國家整體經濟發展，公布此案例，但封閉其他消息']
gov_impact_problem2 = [[10,0,5,3,4,2],[50,30,4,2,2,0], [40,20,2,0,4,2]]
gov_decision_problem3 = ['A國家預算吃緊，無論如何先照舊，有吵再給他們糖吃','B重新審核，但發現真的沒辦法給多少','C為提升疫苗施打率，先補助一點看成效']
gov_impact_problem3 = [[10,0,5,3,4,2],[50,30,4,2,2,0], [40,20,2,0,4,2]]
gov_decision_problem4 = ['A國外好多解封後復發的案例 先不要','B滾動式解封 不管甚麼事情先滾動就對了','C老百姓叫苦連天，就解封吧，地方政府再自己看狀況']
gov_impact_problem4 =[[10,0,5,3,4,2],[50,30,4,2,2,0], [40,20,2,0,4,2]]
gov_decision_problem5 = ['A發明新名詞來彌補落差','B授權地方公布疫調','C投入更多人力，疫調一定沒問題']
gov_impact_problem5 =[[10,0,5,3,4,2],[50,30,4,2,2,0], [40,20,2,0,4,2]]
'''
