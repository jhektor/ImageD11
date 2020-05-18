
"""Autogenerated by src/bldlib.py. Edit in src/cImageD11_interface.pyf please"""
array_histogram = """computes the histogram for an image
"""
array_mean_var_cut = """es
"""
array_stats = """computes statistics for an image.
"""
blob_moments = """fills in the reduced moments in results array.
... FIXME - this would be clearer in python, fast anyway.
"""
bloboverlaps = """determines the overlaps between labels1 and labels2
for an image series. Peaks in labels2 may be merged if they were
joined by a peak on labels1. Results in results1 are accumulated
into results2 if peaks are overlapped.
"""
blobproperties = """fills the array results with properties of each labelled
object described by data (pixel values) and labels. The omega value
is the angle for this frame.
results are FIXME
"""
cimaged11_omp_get_max_threads = """reads the openmp max number of threads
"""
cimaged11_omp_set_num_threads = """Sets the openmp number of threads to use.
Change if you use multiprocessing or do not like os.environ['OMP_NUM_THREADS']
see also: multiprocessing.cpu_count(), os.cpu_count()
"""
clean_mask = """removes pixels which are not 4 connected from msk
while copying into ret.
Beware: work in progress
"""
closest = """finds the value and index in x closest to a value in v.
e.g. x = cosine of angles between pairs of peaks
     v = idealised values based on hkl geometry
  ibest set to the x[i] matching to a v[j] with diff "best"
"""
closest_vec = """finds the closest neighbors for each row of X
ignoring the self. Treated as a X=[v1,v2,v3,...], computes
sum{(vi-vj)**2} for all i!=j and places minimum in ic.
"""
cluster1d = """is used in sandbox/friedel.py to find clusters of peaks
work in progress
"""
compress_duplicates = """removes duplicate i,j labels. On entry then
i and j are set as the labels from two images. They are sorted
and on exit i,j hold the unique pairs and oi holds the count
for the number of overlaps. oj and tmp are temporaries.
"""
compute_gv = """computes scattering vectors given thr positions of the spot
in the laboratory in xlylzl[npks], the omega rotation[npks], and
the rest of the parameters (wedge,wvln,chi,t[3] and omegasign)
"""
computes_xlylzl = """finds spot positions in the laboratory frame
using packed parameters that are more general
s    = slow pixel position
f    = fast pixel position
p    = [s_cen, f_cen, s_size, f_size]
r[9] = dot( transform.detector_rotation_matrix, flipmatrix )
... with flipmatrix = [1,0,0], [0,o22,o21], [0,o12,o11]
dist = [distancex, distancey, distancez] is 3D (beyond old model)
... see test/test_cImageD11.py
"""
connectedpixels = """Determines which pixels in data are above the
user supplied threshold and assigns them into connected objects
which are output in labels. Connectivity is 3x3 box (8) by default
and reduces to a +(4) is con8==0
"""
count_shared = """takes two sorted arrays in pi and pj and counts
how many collisions there are. Useful to compare two lists of
peak to grain assignments, or pixel to peak assignments, etc
"""
frelon_lines = """Subtracts the average value of (pixels < cut) per row
"""
frelon_lines_sub = """Subtracts drk from img and then same as frelon_lines
"""
localmaxlabel = """assigns a label for each pixel so they are grouped
to the local maximum. Equal values choose to assign towards the earlier
value in memory.
cpu arg (1)0=C, (1)1=SSE2, (1)2=AVX2; if > 9 prints timing
"""
make_clean_mask = """is a lot like clean msk but it generates
the msk using img and cut.
Beware: work in progress
"""
mask_to_coo = """takes a mask and converts it to a list
of co-ordinates in a sparse array coo format
"""
misori_cubic = """computes the trace of the smallest misorientation
 for cubic symmetry
 u1 and u2 are both orientation matrices "U"
     compute u1. u2.T  to get the rotation from one to the other
     find the permutation that will maximise the trace
       one of six...
          xyz   yxz   zxy
          xzy   yzx   zyx
Beware : work in progress. Which point group is this?
"""
misori_cubic_pairs = """Computes the dissimilarity matrix to use for clustering
of orientations. Fills in an upper triangular matrix that you can try
to pass to scipy.cluster routines
"""
misori_monoclinic = """assumes a unique b axis and only checks
the flip of b -> -b
Not sure about the point group here. Is is 2/m  ??
 Beware: work in progress
"""
misori_orthorhombic = """computes the trace of the smallest misorientation
 u1 and u2 are both orientation matrices "U"
     compute u1. u2.T  to get the rotation from one to the other
     find the flips that will maximise the trace:
       abs( trace(dot(u1,u2.T) ))
 Looks like point group mmm. Not sure why this is in C?
 Beware: work in progress
"""
misori_tetragonal = """computes the trace of the smallest misorientation
 u1 and u2 are both orientation matrices "U"
     compute u1. u2.T  to get the rotation from one to the other
     finds the flips a/b and c->-c that will maximise the trace:
       abs( trace(dot(u1,u2.T) ))
 Looks like point group 4/mmm. What about 4/m ?
 Beware: work in progress
"""
put_incr32 = """does the simple loop : data[ind] += vals
not sure why this isn't in numpy
uses 32 bit addressing
"""
put_incr64 = """does the simple loop : data[ind] += vals
not sure why this isn't in numpy
uses 64 bit addressing
"""
quickorient = """takes two g-vectors in UBI[0] and UBI[1]
and overwrites with UBI orientation using cache in bt (from h1,h2)
"""
refine_assigned = """fits a ubi matrix to a set of g-vectors and assignments
in labels. e.g. where(labels==label) it uses the peaks.
  ... perhaps this is not what you want for overlapping peaks in twins!
"""
score = """takes a ubi matrix and list of g-vectors and computes
hkl = dot(ubi, gv), then rounds these g-vectors to integer
and computes drlv2 = (h-int(h))**2 + (k-int(k))**2 + (l-int(l))**2
If drlv2 is less than tol*tol then the peak is considered to
be indexed. Returns the number of peaks found.
"""
score_and_assign = """is similar to score but it assigns peaks to this
ubi only if they fit the data better than the current UBI.
It updates drlv2 and labels to use best fitting grain for each peak.
 ... perhaps this is not what you want for overlapping peaks in twins!
"""
score_and_refine = """is very similar to score but it also refines the UB
matrix using the assigned peaks and overwrite the argument.
It returns the number of peaks and fit prior to refinement.
"""
score_gvec_z = """reads ubi, ub, gv and recompute
if (recompute) it fills directions to project errors per peak:
     g0 = gv / |gv|   = unit vector along g
     g1 = gxy / |gxy| = unit vector perpendicular to z
     g2 ... ought to be cross( g0, g1 ) ?
For all peaks it computes h = ubi.g, rounds to nearest ih = int(h)
and then computes gcalc = ub.ih = dot( ub, ( round( dot( ubi, g) ) ) )
The error gv - gcalc is then projected into the co-ordinate system
g0,g1,g2 for errors along g, z and the rhs
Beware : work in progress. Is z always the right axis?
"""
sparse_blob2Dproperties = """fills the array results with properties of each labelled
object described by v and labels (pixel values and blob) and positions i,j in the image.
results are:
  results[ipk,s2D_1]   = sum (1), number of pixels
  results[ipk,s2D_I]   = sum (I), total intensity
  results[ipk,s2D_fI]  = sum (f*I), intensity weighted fast index
  results[ipk,s2D_sI]  = sum (s*I), intensity weighted slow index
  results[ipk,s2D_ffI] = sum (f*f*I), intensity weighted fast^2 index
  results[ipk,s2D_sfI] = sum (s*f*I), intensity weighted slow*fast index
  results[ipk,s2D_ssI] = sum (s*s*I), intensity weighted slow^2 index
"""
sparse_connectedpixels = """runs the connectedpixels algorithm on
a sparse image using a supplied threshold putting labels
into labels array and returning the number of blobs found
"""
sparse_connectedpixels_splat = """is for debugging/timing. It splats the sparse
array into a dense array and runs the old connectedpixels code on that.
"""
sparse_is_sorted = """checks whether the indices in i and j of a sparse
coo format come in the order that they would appear inside an image
"""
sparse_localmaxlabel = """assigns labels to sparse array in sorted coo format
supplied in (v,(i,j)). MV and iMV are temporaries.
single threaded
"""
sparse_overlaps = """identifies the pixels in i1,j1 which overlap i2,j2.
The list of overlaps is returned in k1/k2 such that i1[k1]==i2[k2]
and j1[k1]==j2[k2]. Probably assumes that sparse_is_sorted was true.
"""
splat = """draws gvectors into an rgba image. The horror of maintaining plot3d
over the years motivated this code. See test/demo/tksplat
"""
__all__ = [
    "array_histogram",
    "array_mean_var_cut",
    "array_stats",
    "blob_moments",
    "bloboverlaps",
    "blobproperties",
    "cimaged11_omp_get_max_threads",
    "cimaged11_omp_set_num_threads",
    "clean_mask",
    "closest",
    "closest_vec",
    "cluster1d",
    "compress_duplicates",
    "compute_gv",
    "computes_xlylzl",
    "connectedpixels",
    "count_shared",
    "frelon_lines",
    "frelon_lines_sub",
    "localmaxlabel",
    "make_clean_mask",
    "mask_to_coo",
    "misori_cubic",
    "misori_cubic_pairs",
    "misori_monoclinic",
    "misori_orthorhombic",
    "misori_tetragonal",
    "put_incr32",
    "put_incr64",
    "quickorient",
    "refine_assigned",
    "score",
    "score_and_assign",
    "score_and_refine",
    "score_gvec_z",
    "sparse_blob2Dproperties",
    "sparse_connectedpixels",
    "sparse_connectedpixels_splat",
    "sparse_is_sorted",
    "sparse_localmaxlabel",
    "sparse_overlaps",
    "splat"]