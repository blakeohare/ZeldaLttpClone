using System;
using System.Net;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Documents;
using System.Windows.Ink;
using System.Windows.Input;
using System.Windows.Media;
using System.Collections.Generic;
using System.Windows.Shapes;

namespace Zelda.Map
{
	public class Layer
	{
		private Tile[,] tiles;
		private int width;
		private int height;

		public Layer(int width, int height, Tile[,] tiles)
		{
			this.tiles = tiles;
			this.width = width;
			this.height = height;
		}

		public int Width { get { return this.width; } }
		public int Height { get { return this.height; } }
		public Tile[,] Tiles { get { return this.tiles; } }

		public bool IsRectangleFree(int left, int top, int right, int bottom)
		{
			int colLeft = left >> 4;
			int colRight = right >> 4;
			int rowTop = top >> 4;
			int rowBottom = bottom >> 4;

			List<Barrier> barriers = new List<Barrier>();
			for (int col = colLeft; col <= colRight; ++col)
			{
				for (int row = rowTop; row <= rowBottom; ++row)
				{
					if (this.tiles[col, row].IsCollisionWithRectangle(left, top, right, bottom))
					{
						return false;
					}
				}
			}
			return true;
		}
	}
}