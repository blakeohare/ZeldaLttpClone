using System;
using System.Collections.Generic;
using System.Linq;
using GameLight.Graphics;
using GameLight.Input;
using GameLight.Scene;
using GameLight.Sound;

namespace Zelda.Map
{
	public struct Barrier
	{
		public Barrier(int left, int top, int right, int bottom, bool diagTopLeft, bool diagTopRight, bool diagBottomLeft, bool diagBottomRight)
		{
			this.Left = left;
			this.Top = top;
			this.Right = right;
			this.Bottom = bottom;
			this.Diagonal = diagTopLeft || diagTopRight || diagBottomLeft || diagBottomRight;
			this.TopLeftOpen = diagTopLeft;
			this.TopRightOpen = diagTopRight;
			this.BottomLeftOpen = diagBottomLeft;
			this.BottomRightOpen = diagBottomRight;
		}

		public Barrier Clone(int tileOffsetX, int tileOffsetY)
		{
			int left = tileOffsetX * 16;
			int top = tileOffsetY * 16;

			return new Barrier(
				this.Left + left,
				this.Top + top,
				this.Right + left,
				this.Bottom + top,
				this.TopLeftOpen,
				this.TopRightOpen,
				this.BottomLeftOpen,
				this.BottomRightOpen);
		}

		public bool IntersectsRectangle(int left, int top, int right, int bottom)
		{
			if (right < this.Left || left >= this.Right || bottom < this.Top || top >= this.Bottom)
			{
				return false;
			}
			else if (!this.Diagonal)
			{
				// if the rectangular regions overlap and this isn't a diagonal, we have a collision
				return true;
			}
			else 
			{
				if (this.TopLeftOpen)
				{
					// TODO: the rest of these...
					return false;
				}
				else if (this.TopRightOpen)
				{
					return false;
				}
				else if (this.BottomLeftOpen)
				{
					return false;
				}
				else
				{
					return false;
				}
			}
		}

		public int Left;
		public int Top;
		public int Right;
		public int Bottom;

		public bool Diagonal;
		public bool TopLeftOpen;
		public bool TopRightOpen;
		public bool BottomLeftOpen;
		public bool BottomRightOpen;
	}
}
