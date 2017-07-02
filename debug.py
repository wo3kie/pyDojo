#!/usr/bin/env python

import numpy as np

m = np.array([[1,2,3], [10,20,30], [100,200,300]])

#
# (mT * inT_in * m) - (mT * inT_out) - (outT_in * m) + (out_T * out)
#
# inT * in          - (t, f).T * (t, f) = (f, t) * (t, f) = (f, f)
# inT * out         - (t, f).T * (t, 1) = (f, t) * (t, 1) = (f, 1)
# outT * in         - (t, 1).T * (t, f) = (1, t) * (t, f) = (1, f)
#
# (mT * inT_in * m) - (f, 1).T * (f, f) * (f, 1) = (1, f) * (f, f) * (f, 1)
#                   - (1, f) * (f, 1) = (1, 1)
#
# (mT * inT_out)    - (f, 1).T * (f, 1) = (1, f) * (f, 1) = (1, 1)
#
# (outT_in * m)     - (1, f) * (f, 1) = (1, 1)
#
# (out_T * out)     - (t, 1).T * (t, 1) = (1, t) * (t, 1) = (1, 1)
#



def m(inT_in, inT_out, outT_in, model, out, tick_id):
    a1 = model.T[tick_id, :].dot(inT_in)
    s1 = a.dot(model[:, tick_id])

    s2 = model.T[tick_id, :].dot(inT_out[:, tick_id])

    s3 = outT_in[tick_id, :].dot(model[:, tick_id])

    s4 = out[tick_id, :].dot(out[:, tick_id])

