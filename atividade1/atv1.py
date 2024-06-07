""""
Quantos pixels são colocados na tela por cada uma destas chamadas?

g.drawLine (10, 20, 100, 50);
g.drawRect (10, 10, 8, 5);
g.fillRect       (10, 10, 8, 5);

Resposta da g.drawLine (10, 20, 100, 50):
- usando o algoritmo de Bresenham (raiz quadrada de (x2-x1)ˆ2 + (y2-y1)ˆ2 ) ˜= 95 pixels

Resposta da g.drawRect (10, 10, 8, 5):
- (2 × 8)+ (2 × 5) − 4 = 16 + 10 − 4 = 22 pixels

Resposta da fillRect(10, 10, 8, 5):
- 8 × 5 = 40 pixels
"""