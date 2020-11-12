# Generates an illustration of the empirical distribution
# of a set of data points.
#
# Note: it is assumed that all elements of dps lie between 0 and 1.
def generate_empirical_distribution_illustration(dps, f):
    def println(l):
        f.write(l+'\n')
    def scale(rx, ry):
        println("%f %f scale" % (rx, rx))
    def newpath():
        println("newpath")
    def closepath():
        println("closepath")
    def stroke():
        println("stroke")
    def fill():
        println("fill")
    def clip():
        println("clip")
    def moveto(x, y):
        println("%f %f moveto" % (x, y))
    def lineto(x, y):
        println("%f %f lineto" % (x, y))
    def make_line(x0, y0, x1, y1):
        newpath()
        moveto(x0, y0)
        lineto(x1, y1)
    def setrgb(r, g, b):
        println("%f %f %f setrgb" % (r, g, b))
    def setgray(x):
        println("%f setgray" % x)
    def setlinewidth(x):
        println("%f setlinewidth" % x)
    def make_box(llx, lly, urx, ury):
        println("%f %f moveto" % (llx, lly))
        println("%f %f lineto" % (urx, lly))
        println("%f %f lineto" % (urx, ury))
        println("%f %f lineto" % (llx, ury))
        println("closepath")

    # print EPS header
    println(r"%!PS-Adobe-3.0 EPSF-3.0")
    println(r"%%BoundingBox: 0 0 100 100")
    newpath()
    make_box(0,0,100,100)
    closepath()
    clip()

    scale(100, 100)

    # convert data points into ordered multi set
    N = len(dps)
    assert N > 0
    dps = sorted(dps)
    ordered_multi_set = []
    x = None
    i = 0
    for y in dps:
        if y > x:
            if not x is None:
                ordered_multi_set.append((x, i))
            x = y
            i = 1
        else:
            i += 1
    ordered_multi_set.append((x,i))
    
    # visualize distribution (multi set)
    setlinewidth(0.005)
    # paint diagonal as visual aid
    setgray(0.8)
    newpath()
    moveto(0, 0)
    lineto(1, 1)
    stroke()

    # paint distribution
    setgray(0)
    newpath()
    m_cur = 0.0
    x_cur = -1.0
    newpath()
    moveto(x_cur, m_cur/N)
    for x,k in ordered_multi_set:
        #make_line(x_cur, m_cur/N, x, m_cur/N)
        lineto(x, m_cur/N)
        x_cur = x
        m_cur += k
        lineto(x, m_cur/N)
    lineto(x_cur, 1.0)
    lineto(2.0, 1.0)
    stroke()
    #make_line(x_cur, m_cur/N, 2.0, m_cur/N)
