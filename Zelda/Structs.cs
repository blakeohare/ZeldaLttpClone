using System;
using System.Net;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Documents;
using System.Windows.Ink;
using System.Windows.Input;
using System.Windows.Media;
using System.Windows.Media.Animation;
using System.Windows.Shapes;

namespace Zelda
{
	public struct Point
	{
		public Point(double x, double y)
		{
			this.X = x;
			this.Y = y;
		}

		public double X;
		public double Y;
	}
}
