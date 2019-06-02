using System;
using System.Collections.Generic;
using System.Linq;
using GameLight.Graphics;
using GameLight.Input;
using GameLight.Scene;
using GameLight.Sound;
using Zelda.Map;

namespace Zelda.Sprites
{
	public abstract class Sprite
	{
		public double X { get; set; }
		public double Y { get; set; }
		public double DX { get; set; }
		public double DY { get; set; }
		public double CollisionRadius { get; set; }

		protected Direction direction;
		public Direction Direction { get { return this.direction; } }
		
		private static readonly Dictionary<Direction, string> directions = new Dictionary<Direction,string>()
		{
			{ Direction.Left, "left" },
			{ Direction.Up, "up" },
			{ Direction.Right, "right" },
			{ Direction.Down, "down" }
		};

		public string DirectionString { get { return directions[this.direction]; } }



		public int RenderLeft { get { return (int)(this.X + this.renderOffset.X); } }
		public int RenderTop { get { return (int)(this.Y + this.renderOffset.Y); } }
		public int Width { get { return (int)(this.CollisionRadius * 2); } }
		public int Height { get { return (int)(this.CollisionRadius * 2); } }
		public Layer Layer
		{
			get { return this.layer; }
			set { this.layer = value; }
		}

		private Level level;
		private Layer layer;

		public Sprite(double x, double y, double radius, Level level, Layer layer)
		{
			this.CollisionRadius = radius;
			this.X = x;
			this.Y = y;
			this.renderOffset = new Point(-radius, -radius);
			this.level = level;
			this.layer = layer;
		}

		public abstract void Update();
		public abstract void Render(Image screen, int cameraOffsetX, int cameraOffsetY);

		private Point renderOffset;
		public virtual Point RenderOffset
		{
			get
			{
				return this.renderOffset;
			}
		}

		public void MoveRequest()
		{
			double x = this.X + this.DX;
			double y = this.Y + this.DY;

			int left = (int)(x - this.CollisionRadius);
			int top = (int)(y - this.CollisionRadius);
			int right = left + (int)(this.CollisionRadius * 2);
			int bottom = top + (int)(this.CollisionRadius * 2);

			if (this.layer.IsRectangleFree(left, top, right, bottom))
			{
				this.X = x;
				this.Y = y;
			}
		}
	}
}
