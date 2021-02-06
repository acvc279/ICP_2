import numpy
l = numpy.random.randint(1,20,20)
print("List: ", l)
r = l.reshape((4,5))
print("reshape:\n", r)
rp_mx = numpy.where(r == numpy.amax(r, axis=1, keepdims=True), 0, r)
print("Max Replacing:\n",rp_mx)