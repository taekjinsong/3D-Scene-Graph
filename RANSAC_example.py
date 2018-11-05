import numpy as np
import pcl

points = np.array([[  594.6663 , -1617.9456 ,  -797.36224],
       [  600.5656 , -1638.1005 ,  -806.5441 ],
       [  599.16583, -1638.3135 ,  -805.9235 ],
       [  597.76605, -1638.5264 ,  -805.3029 ],
       [  596.36633, -1638.7394 ,  -804.6823 ],
       [  594.96655, -1638.9523 ,  -804.06165],
       [  593.5668 , -1639.1652 ,  -803.44104],
       [  592.16705, -1639.3782 ,  -802.82043],
       [  590.7673 , -1639.5911 ,  -802.1998 ],
       [  589.36755, -1639.804  ,  -801.5792 ],
       [  587.9678 , -1640.017  ,  -800.9586 ],
       [  586.568  , -1640.2299 ,  -800.338  ],
       [  595.3116 , -1618.2574 ,  -796.01373],
       [  601.2189 , -1638.4161 ,  -805.1791 ],
       [  599.8191 , -1638.6292 ,  -804.5585 ],
       [  598.4193 , -1638.842  ,  -803.9378 ],
       [  597.0196 , -1639.055  ,  -803.3172 ],
       [  595.6198 , -1639.268  ,  -802.6966 ],
       [  594.22003, -1639.4808 ,  -802.076  ],
       [  592.8203 , -1639.6938 ,  -801.4554 ],
       [  591.42053, -1639.9067 ,  -800.8348 ],
       [  590.0208 , -1640.1196 ,  -800.2142 ],
       [  588.62103, -1640.3326 ,  -799.5935 ],
       [  587.22125, -1640.5455 ,  -798.9729 ],
       [  595.9569 , -1618.5692 ,  -794.6653 ],
       [  598.22314, -1628.7557 ,  -798.9331 ],
       [  596.8319 , -1628.9674 ,  -798.3162 ],
       [  599.0726 , -1639.1577 ,  -802.57275],
       [  597.67285, -1639.3707 ,  -801.95215],
       [  596.2731 , -1639.5836 ,  -801.33154],
       [  594.8733 , -1639.7965 ,  -800.71094],
       [  593.4736 , -1640.0095 ,  -800.0903 ],
       [  592.0738 , -1640.2224 ,  -799.46967],
       [  590.674  , -1640.4353 ,  -798.84906],
       [  589.2743 , -1640.6483 ,  -798.22845],
       [  584.31067, -1630.8721 ,  -792.7647 ],
       [  600.2637 , -1628.8579 ,  -798.1932 ],
       [  598.87244, -1629.0695 ,  -797.5763 ],
       [  597.4812 , -1629.2811 ,  -796.9595 ],
       [  599.7258 , -1639.4734 ,  -801.2077 ],
       [  598.3261 , -1639.6864 ,  -800.5871 ],
       [  596.92633, -1639.8993 ,  -799.96643],
       [  595.52655, -1640.1122 ,  -799.3458 ],
       [  594.12683, -1640.3252 ,  -798.7252 ],
       [  592.72705, -1640.5381 ,  -798.1046 ],
       [  587.74243, -1630.7626 ,  -792.6416 ],
       [  586.3512 , -1630.9742 ,  -792.0248 ],
       [  584.95996, -1631.1859 ,  -791.4079 ],
       [  600.91296, -1629.1716 ,  -796.83636],
       [  599.5217 , -1629.3833 ,  -796.21954],
       [  598.1305 , -1629.5948 ,  -795.6027 ],
       [  596.7392 , -1629.8065 ,  -794.98584],
       [  595.34796, -1630.0182 ,  -794.369  ],
       [  593.9567 , -1630.2299 ,  -793.7522 ],
       [  592.5655 , -1630.4414 ,  -793.1353 ],
       [  591.17426, -1630.6531 ,  -792.5185 ],
       [  589.78296, -1630.8647 ,  -791.9017 ],
       [  588.3917 , -1631.0764 ,  -791.28485],
       [  587.0005 , -1631.288  ,  -790.66797],
       [  585.60925, -1631.4996 ,  -790.05115],
       [  601.56226, -1629.4854 ,  -795.4796 ],
       [  600.171  , -1629.697  ,  -794.8628 ],
       [  598.7797 , -1629.9087 ,  -794.2459 ],
       [  597.3885 , -1630.1202 ,  -793.6291 ],
       [  595.99725, -1630.3319 ,  -793.01227],
       [  594.606  , -1630.5436 ,  -792.3954 ],
       [  593.2148 , -1630.7552 ,  -791.77856],
       [  591.82355, -1630.9668 ,  -791.16174],
       [  590.43225, -1631.1785 ,  -790.54486],
       [  589.041  , -1631.3901 ,  -789.92804],
       [  587.6498 , -1631.6018 ,  -789.3112 ],
       [  586.25854, -1631.8134 ,  -788.6944 ],
       [  598.53815, -1619.8167 ,  -789.27136],
       [  597.15546, -1620.027  ,  -788.6583 ],
       [  595.7727 , -1620.2373 ,  -788.0452 ],
       [  598.0378 , -1630.4341 ,  -792.27234],
       [  596.64655, -1630.6456 ,  -791.65546],
       [  595.2553 , -1630.8573 ,  -791.03864],
       [  593.8641 , -1631.069  ,  -790.4218 ],
       [  592.4728 , -1631.2806 ,  -789.80493],
       [  591.08154, -1631.4922 ,  -789.1881 ],
       [  589.6903 , -1631.7039 ,  -788.5713 ],
       [  588.2991 , -1631.9155 ,  -787.9544 ],
       [  583.32806, -1622.1304 ,  -782.52765],
       [  599.1835 , -1620.1284 ,  -787.9229 ],
       [  597.8007 , -1620.3387 ,  -787.3098 ],
       [  596.418  , -1620.5491 ,  -786.6968 ],
       [  598.6871 , -1630.7478 ,  -790.9155 ],
       [  597.29584, -1630.9595 ,  -790.2987 ],
       [  595.9046 , -1631.171  ,  -789.6819 ],
       [  594.5133 , -1631.3827 ,  -789.065  ],
       [  593.1221 , -1631.5944 ,  -788.4482 ],
       [  588.1216 , -1621.8112 ,  -783.0184 ],
       [  586.7389 , -1622.0215 ,  -782.40533],
       [  585.35614, -1622.2319 ,  -781.79224],
       [  583.9734 , -1622.4423 ,  -781.1792 ],
       [  599.8288 , -1620.4403 ,  -786.57446],
       [  598.44604, -1620.6506 ,  -785.96136],
       [  597.0633 , -1620.861  ,  -785.3483 ],
       [  595.6806 , -1621.0713 ,  -784.7352 ],
       [  594.29785, -1621.2816 ,  -784.1222 ],
       [  592.9151 , -1621.492  ,  -783.5091 ],
       [  591.5324 , -1621.7024 ,  -782.89606],
       [  590.14966, -1621.9127 ,  -782.28296],
       [  588.7669 , -1622.123  ,  -781.6699 ],
       [  587.38416, -1622.3334 ,  -781.0568 ],
       [  586.00146, -1622.5437 ,  -780.4438 ],
       [  584.6187 , -1622.754  ,  -779.8307 ],
       [  600.4741 , -1620.7521 ,  -785.22595],
       [  599.0914 , -1620.9624 ,  -784.6129 ],
       [  597.7086 , -1621.1729 ,  -783.9998 ],
       [  596.3259 , -1621.3832 ,  -783.3868 ],
       [  594.9432 , -1621.5935 ,  -782.7737 ],
       [  593.5604 , -1621.8038 ,  -782.16064],
       [  592.1777 , -1622.0142 ,  -781.54755],
       [  590.795  , -1622.2245 ,  -780.9345 ],
       [  589.41223, -1622.4348 ,  -780.3214 ],
       [  588.0295 , -1622.6453 ,  -779.7084 ],
       [  586.6467 , -1622.8556 ,  -779.0953 ],
       [  585.26404, -1623.0659 ,  -778.48224],
       [  601.11945, -1621.064  ,  -783.8775 ],
       [  599.7367 , -1621.2743 ,  -783.2644 ],
       [  598.35394, -1621.4846 ,  -782.65137],
       [  596.9712 , -1621.695  ,  -782.03827],
       [  595.5885 , -1621.9053 ,  -781.42523],
       [  594.20575, -1622.1157 ,  -780.81213],
       [  592.823  , -1622.326  ,  -780.1991 ],
       [  591.44025, -1622.5364 ,  -779.586  ],
       [  590.05756, -1622.7467 ,  -778.97296],
       [  588.6748 , -1622.957  ,  -778.35986],
       [  587.29205, -1623.1674 ,  -777.7468 ],
       [  582.3137 , -1613.3733 ,  -772.357  ],
       [  601.7647 , -1621.3757 ,  -782.529  ],
       [  600.382  , -1621.5862 ,  -781.91595],
       [  598.99927, -1621.7965 ,  -781.30286],
       [  597.6165 , -1622.0068 ,  -780.6898 ],
       [  596.23376, -1622.2172 ,  -780.0767 ],
       [  594.8511 , -1622.4275 ,  -779.4637 ],
       [  593.4683 , -1622.6378 ,  -778.8506 ],
       [  592.0856 , -1622.8481 ,  -778.23755],
       [  590.7028 , -1623.0586 ,  -777.6245 ],
       [  589.3201 , -1623.2689 ,  -777.0114 ],
       [  584.3293 , -1613.4741 ,  -771.6261 ],
       [  582.9551 , -1613.6832 ,  -771.01685],
       [  602.41003, -1621.6876 ,  -781.18054],
       [  601.0273 , -1621.898  ,  -780.5675 ],
       [  599.6446 , -1622.1083 ,  -779.9544 ],
       [  598.26184, -1622.3186 ,  -779.3414 ],
       [  596.8791 , -1622.529  ,  -778.7283 ],
       [  595.49634, -1622.7394 ,  -778.11523],
       [  594.11365, -1622.9497 ,  -777.50214],
       [  592.7309 , -1623.16   ,  -776.8891 ],
       [  591.34814, -1623.3704 ,  -776.276  ],
       [  589.96545, -1623.5807 ,  -775.66296],
       [  584.9706 , -1613.784  ,  -770.28595],
       [  583.5964 , -1613.9932 ,  -769.67664],
       [  603.05536, -1621.9995 ,  -779.8321 ],
       [  601.6726 , -1622.2098 ,  -779.219  ],
       [  600.28986, -1622.4202 ,  -778.60596],
       [  598.90717, -1622.6305 ,  -777.99286],
       [  597.5244 , -1622.8408 ,  -777.3798 ],
       [  596.14166, -1623.0511 ,  -776.7667 ],
       [  591.1088 , -1613.2578 ,  -771.38293],
       [  589.7346 , -1613.4668 ,  -770.7737 ],
       [  588.3604 , -1613.6759 ,  -770.16437],
       [  586.98615, -1613.885  ,  -769.55505],
       [  585.61194, -1614.094  ,  -768.9458 ],
       [  584.23773, -1614.3031 ,  -768.3365 ],
       [  603.7007 , -1622.3113 ,  -778.4836 ],
       [  602.31793, -1622.5216 ,  -777.87054],
       [  600.9352 , -1622.7319 ,  -777.25745],
       [  599.5525 , -1622.9423 ,  -776.6444 ],
       [  598.16974, -1623.1527 ,  -776.0313 ],
       [  596.787  , -1623.363  ,  -775.4183 ],
       [  591.7502 , -1613.5677 ,  -770.0428 ],
       [  590.376  , -1613.7767 ,  -769.4335 ],
       [  589.0017 , -1613.9858 ,  -768.8242 ],
       [  587.6275 , -1614.1948 ,  -768.2149 ],
       [  586.2533 , -1614.4039 ,  -767.6056 ],
       [  584.8791 , -1614.6129 ,  -766.99634]], dtype=np.float32)