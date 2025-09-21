import dp_compendium.viterbi_hmm as vit
def test_runs():
    states=['H','C']
    start={'H':0.6,'C':0.4}
    trans={'H':{'H':0.7,'C':0.3},'C':{'H':0.4,'C':0.6}}
    emit={'H':{'A':0.2,'B':0.8},'C':{'A':0.5,'B':0.5}}
    path = vit.viterbi(states,start,trans,emit,['A','B','A','B'])
    assert len(path)==4
