import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import streamlit as st

class ControlBrake:

    def __init__(self):
        self.carPos=ctrl.Antecedent(np.arange(0,61,1),'carPos')
        self.carVel=ctrl.Antecedent(np.arange(0,101,1),'carVel')
        self.brakeForce=ctrl.Consequent(np.arange(0,9264,1),'brakeForce')
        self.brakesystem_simulator = None

    
    def setRules(self):
        self.carPos['muycerca']=fuzz.gauss2mf(self.carPos.universe,-2.76,10,3.773,3.86)
        self.carPos['cerca']=fuzz.gaussmf(self.carPos.universe,18.42,4.21)
        self.carPos['medio']=fuzz.gaussmf(self.carPos.universe,27.76,3.96)
        self.carPos['lejos']=fuzz.gaussmf(self.carPos.universe,38,3.54)
        self.carPos['muylejos']=fuzz.gauss2mf(self.carPos.universe,51,3.46,63.3,5.1)   

        self.carVel['muylento']=fuzz.gauss2mf(self.carVel.universe,-0.153,10,7.945,4.02)
        self.carVel['lento']=fuzz.gaussmf(self.carVel.universe,27.97,6.6)
        self.carVel['medio']=fuzz.gaussmf(self.carVel.universe,42.26,11.3)
        self.carVel['rapido']=fuzz.gaussmf(self.carVel.universe,53.6,7.177)
        self.carVel['muyrapido']=fuzz.gauss2mf(self.carVel.universe,68.18,4.04,103.6,6.48)


        self.brakeForce['pequeño']=fuzz.gaussmf(self.brakeForce.universe,2530,730.4)
        self.brakeForce['mediano']=fuzz.gaussmf(self.brakeForce.universe,4760,1325)
        self.brakeForce['grande']=fuzz.gaussmf(self.brakeForce.universe,6120,1090)


        rule1 = ctrl.Rule(self.carPos['muycerca'] & self.carVel['muylento'] , self.brakeForce['pequeño'])
        rule2 = ctrl.Rule(self.carPos['muycerca'] & self.carVel['lento'] , self.brakeForce['pequeño'])
        rule3 = ctrl.Rule(self.carPos['muycerca'] & self.carVel['medio'] , self.brakeForce['pequeño'])
        rule4 = ctrl.Rule(self.carPos['muycerca'] & self.carVel['rapido'] , self.brakeForce['mediano'])
        rule5 = ctrl.Rule(self.carPos['muycerca'] & self.carVel['muyrapido'] , self.brakeForce['mediano'])


        rule6 = ctrl.Rule(self.carPos['cerca'] & self.carVel['muylento'] , self.brakeForce['pequeño'])
        rule7 = ctrl.Rule(self.carPos['cerca'] & self.carVel['lento'] , self.brakeForce['pequeño'])
        rule8 = ctrl.Rule(self.carPos['cerca'] & self.carVel['medio'] , self.brakeForce['pequeño'])
        rule9 = ctrl.Rule(self.carPos['cerca'] & self.carVel['rapido'] , self.brakeForce['mediano'])
        rule10 = ctrl.Rule(self.carPos['cerca'] & self.carVel['muyrapido'] , self.brakeForce['mediano'])

        rule11 = ctrl.Rule(self.carPos['medio'] & self.carVel['muylento'] , self.brakeForce['pequeño'])
        rule12 = ctrl.Rule(self.carPos['medio'] & self.carVel['lento'] , self.brakeForce['pequeño'])
        rule13 = ctrl.Rule(self.carPos['medio'] & self.carVel['medio'] , self.brakeForce['mediano'])
        rule14 = ctrl.Rule(self.carPos['medio'] & self.carVel['rapido'] , self.brakeForce['grande'])
        rule15 = ctrl.Rule(self.carPos['medio'] & self.carVel['muyrapido'] , self.brakeForce['grande'])


        rule16 = ctrl.Rule(self.carPos['lejos'] & self.carVel['muylento'] , self.brakeForce['mediano'])
        rule17 = ctrl.Rule(self.carPos['lejos'] & self.carVel['lento'] , self.brakeForce['mediano'])
        rule18 = ctrl.Rule(self.carPos['lejos'] & self.carVel['medio'] , self.brakeForce['grande'])
        rule19 = ctrl.Rule(self.carPos['lejos'] & self.carVel['rapido'] , self.brakeForce['grande'])
        rule20 = ctrl.Rule(self.carPos['lejos'] & self.carVel['muyrapido'] , self.brakeForce['grande'])

        rule21 = ctrl.Rule(self.carPos['muylejos'] & self.carVel['muylento'] , self.brakeForce['mediano'])
        rule22 = ctrl.Rule(self.carPos['muylejos'] & self.carVel['lento'] , self.brakeForce['mediano'])
        rule23 = ctrl.Rule(self.carPos['muylejos'] & self.carVel['medio'] , self.brakeForce['grande'])
        rule24 = ctrl.Rule(self.carPos['muylejos'] & self.carVel['rapido'] , self.brakeForce['grande'])
        rule25 = ctrl.Rule(self.carPos['muylejos'] & self.carVel['muyrapido'] , self.brakeForce['grande'])

        brakesystem_ctrl=ctrl.ControlSystem([rule1,rule2,
                                            rule3,rule4,rule5,
                                            rule6,rule7,
                                            rule8,rule9,rule10,
                                            rule11,rule12,
                                            rule13,rule14,rule15,
                                            rule16,rule17,
                                            rule18,rule19,rule20,
                                            rule21,rule22,
                                            rule23,rule24,rule25])
        self.brakesystem_simulator=ctrl.ControlSystemSimulation(brakesystem_ctrl)

    def determine(self, speed, distance):
        self.carPos.terms['muycerca'].mf
        for t in self.carPos.terms:
            mval=np.interp(distance,self.carPos.universe,self.carPos[t].mf)
            print(t,mval)

        for t in self.carVel.terms:
            mval=np.interp(speed,self.carVel.universe,self.carVel[t].mf)
            print(t,mval)

        self.brakesystem_simulator.input['carPos']=distance
        self.brakesystem_simulator.input['carVel']=speed

        self.brakesystem_simulator.compute()

        return self.brakesystem_simulator.output['brakeForce']