#purely functional Bayesian classifier
#complete fit function

fit = lambda cases,classes:\
        {
            "cl":[x for x in range(len(cases[0]))],###
            "clprob":[x for x in range(len(list(set(classes))))],
            "features":len([x for x in range(len(cases[0]))]),
            "classes":list(set(classes)),
        }
predict = lambda clf, vectors: \
        [max(_bayesian_probabilities(clf,case)) for case in vectors]
_bayesian_probabilities = lambda clf,case: \
        [_bayesian(clf,case,cl) for cl in range(len(clf['classes']))]
_bayesian = lambda clf,case,cl: \
        clf['clprob'][cl]*product (clf['cl'][feat] for feature in range(clf['features']))

product = lambda x: product((x[0]*x[1],)+tuple(x[2:])) if len(x)>2 else x[0]*x[1]
