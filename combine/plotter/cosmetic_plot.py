import os, sys
import argparse 
import numpy as np
sys.path.append('../../')

from ROOT import TH1F, TFile, TCanvas, TLegend, THStack

from tools.style_manager import *
import tools.tdrstyle as tdr
tdr.setTDRStyle()

###################
## Initialisation
###################

parser = argparse.ArgumentParser()
parser.add_argument('inputname', help='display your input file')
parser.add_argument('observable', help='display your observable')

args = parser.parse_args()
inputname = args.inputname
observable = args.observable

###################
## Inputs
###################

#observable = raw_input('Choose your observable : ')
#print observable


###################
## Body
###################

canvas = TCanvas(observable, observable, 600, 600)
inputfile = TFile(inputname)
histogram = inputfile.Get(observable)

if observable.find('m_dilep') != -1:
    title = 'dilepton mass' 
elif  observable.find('n_bjets') != -1:
    title = 'b-jets multiplicity'

leg = 't#bar{t} signal strength'
header = 'Asimov 2017'

# cosmetic
histogram.SetName('')
histogram.SetTitle(title)

legend = TLegend(0.5,0.9,0.9,0.75)
legend.SetHeader(header, 'C')
legend.AddEntry(histogram, leg, 'lep')

stack = THStack()
stack.Add(histogram)
stack.Draw('E HIST')
legend.Draw('SAME')

stack.SetMinimum(0.95)
stack.SetMaximum(1.05)

style_histo(histogram, 1, 1, 0, 3001, 1, 20)
tdr.cmsPrel(41530., 13.)
style_labels_counting(stack, 'r (signal strengh)', 'sidereal time (h)')


raw_input('exit')

canvas.SaveAs('./out/'+observable+'.png')