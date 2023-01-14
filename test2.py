import pickle

with open('extractorPDF.sav', 'rb') as f:
    report = pickle.load(f)
    
report.run('F:/BRAC Undergraduate Courses/Thesis/Project/ParserPDF/file.pdf')