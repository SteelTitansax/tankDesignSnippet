
if __name__ == '__main__':

# Variable declaration
#---------------------
    # Note hacer esto en funcion del esquema geometrico de un tanque
    # ---------------------------------------------------------------------

    extTankH = 3 # m
    extTankR = 1.5 # m
    nominalCapacity = 11850 # l
    criogenicalFactorCapacity = 0.95
    pi = 3.1416
    Vcilinder = pi * pow(extTankR,2) * extTankH
    Vdome = (2/3) * pi * pow(extTankR,3)
    T = 298 #Kº
    V = (Vcilinder + Vdome) * 1000 #L
    print('V',V)
    workingPressure = 10 #atm
    n = (workingPressure * V)/(0.0821 * T)
    print('n',n)
    nitrogenMolesMass = 28 #g/mol
    m = n * nitrogenMolesMass * 0.001 #Kg
    print('m',m)
    stealThickness = 0.01 #m
    AreaSteel = 2*pi*extTankR*extTankH + 3*pi*extTankR*extTankR
    print('AreaSteel',AreaSteel)
    Vsteel = AreaSteel * stealThickness
    print('Vsteel',Vsteel)
    steelDensity = 7850 #kg/m3
    isolatematerialDensity = 100 #kg/m3
    isolateMaterialThickness = 0.05  # mm
    VexternalTank = pi * pow((extTankR + isolateMaterialThickness),2) * extTankH + ((2/3) * pi * pow(extTankR + isolateMaterialThickness,3))
    print('vexternalTank',VexternalTank)
    VinternalTank = (pi * pow(extTankR,2) * extTankH )+ ((2/3) * pi * pow(extTankR,3))
    print('VinternalTank', VinternalTank)
    Visolation = VexternalTank - VinternalTank
    print('vIsolation', Visolation)
    metalicWeight = Vsteel * steelDensity  # kg
    print('metalicweight',metalicWeight)
    isolatingMaterialWeight = Visolation * isolatematerialDensity # kg
    print('isolatingmaterialwieght', isolatingMaterialWeight)
    emptyTankWeight = isolatingMaterialWeight + metalicWeight
    print('emptyTankWeight', emptyTankWeight)
    fullTankWeight = emptyTankWeight + m
    print('fullTankWeight',fullTankWeight)



    # Building material acerinox AISI 304
    # -----------------------------------
    # Cloak design / Diseño de manto
    # ------------------------------
    # Tanque interno
    # ------------------------------
    # Cloak design / Diseño de manto
    # ------------------------------
    # t = P R / (S * E - 0.6 * P)

    # P = Design Pressure , equal to 84.26 lbs/inch^2
    P = 84.26 # lbs/inch^2
    # R = External cloack radius equal to 38.03 inches ( 965.962 mm )
    R = 38.03 # inches
    # S = Working effort admisible for ACERINOX AISI 304 in relation with temperature
    # in this case equal to 18800 lbs/inch^2, this value is extrated form UCS-23 (appendix B.2)
    S = 18800 # lbs/inch^2
    # E = Efficiency of the welded joint
    E = 0.85

    t = P * R / ( (S * E) - 0.6 * P)

    print("Cloak",t,"inches")
    print("Cloak", t * 25.1, "inches")

# Domus design / diseño del domo
# ------------------------------
    # t = (P * D) / ((2*S*E) - (0.2 *P))
    # P: Design pressure in this case 84.26 lbs/inches^2
    P = 84.26 # lbs/inches^2
    # D: External domus diameter in this case 76.063 inches
    D = 76.063 # inches
    # S: Working effort permissible for ACERINOX AISI 304 in relation with temperature (18800 lbs/inch^2)
    S = 18800 # lbs/inches^2
    # E: Joint efficiency weldered equal to 0.85
    E = 0.85

    t = (P * D) / ((2*S*E) - (0.2 *P))

    print("Domus",t,"inches")
    print("Domus", t * 25.1, "inches")


# Breastplate design
# --------------------------------

# Cloak design / Diseño de manto
# ------------------------------

    # Pa = (4 * B)/(3*(Do/t))

    # Pa = maximum pressure admited for the cloak compared with the external.

    # Adimensional factor (4000) L/Do = 2.137 L =4800mm Do = 2246 mm (88.43 inches)

    # Do/t = 187.19 , in this case t = 0.4724 inches (12 mm)

    # A = 0.000125 B = 3625
    B = 3625
    # Do external tank diameter
    Do = 88.43 #inches
    t = 0.4726
    Pa = (4 * B)/((3*Do)/t)

    print("Pa (maximum pressure cloak admited)", Pa, "lbs/inches^2")

    # Domus design / Diseño del domo
    # -------------------------------------------

    # Pa = B/(Ro/t)

    B = 6000
    Ro = 1796.8
    t = 6

    Pa = B/(Ro/t)

    print("Pa (maximum pressure domus admited)", Pa, "lbs/inches^2")

    # Thermal design / Diseño termico
    # ---------------------------------------

    #  Thermal isolating with expanded perlita with an average density of 142 mm

    # q = ((Tamb - Tnitro)/Rtot) * Lc

    # Tamb = ambient temperature , we are assuming 35 Cª
    Tamb = 35
    # TNitro = nitrogen temperature equal -196 Cº
    Tnitro = -196
    # R'tot = defined by the sum of convective resistances of nitrogen and environment.
    # conductive resistances of an internal tank, thermal isolating. breastplate

    # R'tot  = ( Ln(R1ext/R1int) / 2 * Pi * k1 ) + ( Ln(R2ext / R2int) / (2 * Pi * ka ) ) + ( Ln(R2ext / R2int) /  (2 * Pi * k2 ) ) + ( 1 / (2 * Pi * hamb * R2ext ) )
    # R2int = Internal Radius breastplate
    # R2ext = External radius breastplate

    # Extracted from C Appendix
    # k1 = 9.2 W/m.ºK (corresponding to AISI steal 304 at 100ºK)
    # k2 = 60.5 W/m.ºK (corresponding to ASTM A-36 steal at 300ºK)
    # kisolation = 0.016 W/m^2*ºK (corresponding to perlita at 100ºK)
    Rtot= 1.3928
    Lc = 4.55
    q = ((Tamb - Tnitro)/Rtot) * Lc

    print('Heat Exchange (q)',q)