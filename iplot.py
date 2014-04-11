#!/usr/bin/env python
# -*- coding: utf-8 -*-
# generated by wxGlade 0.6.4 on Fri Apr 11 11:58:53 2014

import wx
import Gnuplot
import math

ID_SLIDER_1 = wx.NewId()
ID_SLIDER_2 = wx.NewId()
ID_SLIDER_3 = wx.NewId()
ID_SLIDER_4 = wx.NewId()
ID_SLIDER_5 = wx.NewId()
ID_SLIDER_6 = wx.NewId()
ID_SLIDER_7 = wx.NewId()

# begin wxGlade: extracode
# end wxGlade


class MyFrame(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: MyFrame.__init__
        kwds["style"] = wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.slider_1 = wx.Slider(self, ID_SLIDER_1, 25, 0, 100, style=wx.SL_VERTICAL | wx.SL_LABELS)
        self.slider_2 = wx.Slider(self, ID_SLIDER_2, 35, 0, 100, style=wx.SL_VERTICAL | wx.SL_LABELS)
        self.slider_3 = wx.Slider(self, ID_SLIDER_3, 55, 0, 100, style=wx.SL_VERTICAL | wx.SL_LABELS)
        self.slider_4 = wx.Slider(self, ID_SLIDER_4, 40, 0, 100, style=wx.SL_VERTICAL | wx.SL_LABELS)
        self.slider_5 = wx.Slider(self, ID_SLIDER_5, 77, 0, 100, style=wx.SL_VERTICAL | wx.SL_LABELS)
        self.slider_6 = wx.Slider(self, ID_SLIDER_6, 40, 0, 100, style=wx.SL_VERTICAL | wx.SL_LABELS)
        self.slider_7 = wx.Slider(self, ID_SLIDER_7, 0, 0, 100, style=wx.SL_VERTICAL | wx.SL_LABELS)

        self.__set_properties()
        self.__do_layout()
        # end wxGlade

	wx.EVT_SLIDER(self, ID_SLIDER_1, self.update)
        wx.EVT_SLIDER(self, ID_SLIDER_2, self.update)
        wx.EVT_SLIDER(self, ID_SLIDER_3, self.update)
        wx.EVT_SLIDER(self, ID_SLIDER_4, self.update)
        wx.EVT_SLIDER(self, ID_SLIDER_5, self.update)
        wx.EVT_SLIDER(self, ID_SLIDER_6, self.update)
        wx.EVT_SLIDER(self, ID_SLIDER_7, self.update)

	self.g = Gnuplot.Gnuplot()
	self.g('set xrange [-30:30]')
	self.g('set yrange [-30:30]')
	self.g('set style data dots')
	# do first plot
        xy = []
        t = 0.5 * 2 * math.pi
        a = self.slider_1.GetValue() / 100. * 2
        b = self.slider_2.GetValue() / 100. * 2
        c = self.slider_3.GetValue() / 100. * 4
        d = self.slider_4.GetValue() / 100. * 2
        e = self.slider_5.GetValue() / 100. * 2
	f = self.slider_6.GetValue() / 100. * 20
        while (t < 2.5 * 2 * math.pi):
            x = a*t*math.sin(c*t**d) + b*math.sin(f*t**e)
            y = a*t*math.cos(c*t**d) + b*math.cos(f*t**e)
            xy.append([x,y])
            t += 4*math.pi / 5000.
        self.g.plot(xy)


    def __set_properties(self):
        # begin wxGlade: MyFrame.__set_properties
        self.SetTitle("frame_1")
        self.SetSize((240, 240))
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: MyFrame.__do_layout
        grid_sizer_1 = wx.GridSizer(1, 7, 0, 0)
        grid_sizer_1.Add(self.slider_1, 0, wx.EXPAND, 0)
        grid_sizer_1.Add(self.slider_2, 0, wx.EXPAND, 0)
        grid_sizer_1.Add(self.slider_3, 0, wx.EXPAND, 0)
        grid_sizer_1.Add(self.slider_4, 0, wx.EXPAND, 0)
        grid_sizer_1.Add(self.slider_5, 0, wx.EXPAND, 0)
        grid_sizer_1.Add(self.slider_6, 0, wx.EXPAND, 0)
        grid_sizer_1.Add(self.slider_7, 0, wx.EXPAND, 0)
        self.SetSizer(grid_sizer_1)
        self.Layout()
        # end wxGlade

    def update(self,event):
	# put your function here!
	xy = []
	t = 0.5 * 2 * math.pi
	a = self.slider_1.GetValue() / 100. * 2
	b = self.slider_2.GetValue() / 100. * 2
	c = self.slider_3.GetValue() / 100. * 4
	d = self.slider_4.GetValue() / 100. * 2
	e = self.slider_5.GetValue() / 100. * 2
	f = self.slider_6.GetValue() / 100. * 20
	while (t < 2.5 * 2 * math.pi):
	    x = a*t*math.sin(c*t**d) + b*math.sin(f*t**e)
	    y = a*t*math.cos(c*t**d) + b*math.cos(f*t**e)
	    xy.append([x,y])
	    t += 4*math.pi / 5000.
        self.g.plot(xy)

# end of class MyFrame
if __name__ == "__main__":
    app = wx.PySimpleApp(0)
    wx.InitAllImageHandlers()
    frame_1 = MyFrame(None, -1, "")
    app.SetTopWindow(frame_1)
    frame_1.Show()
    app.MainLoop()
