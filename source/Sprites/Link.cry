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
	public class Link : Sprite
	{
		private enum State
		{
			Standing,
			Walking
		}

		private State state;
		private int renderCounter = 0;
		private int lifetimeCounter = 0;

		public Link(double x, double y, Level level, Layer layer)
			: base(x, y, 7, level, layer)
		{
			this.state = State.Standing;
			this.direction = Direction.Down;
		}

		public override void Update()
		{
			this.lifetimeCounter++;
		}

		public void SetWalkingDirection(double dx, double dy)
		{
			if (dx == 0 && dy == 0)
			{
				this.state = State.Standing;
			}
			else
			{
				this.state = State.Walking;

				// TODO: there needs to be better direction logic here
				// when multiple directions are pressed, the correct final direction
				// should be the first direction applied that is still active.
				// With this current mechanism, left+right gets dominance over up+down
				if (dx < 0) this.direction = Direction.Left;
				else if (dx > 0) this.direction = Direction.Right;
				else if (dy > 0) this.direction = Direction.Down;
				else if (dy < 0) this.direction = Direction.Up;
			}

			this.DX = dx;
			this.DY = dy;
		}

		public override void Render(GameLight.Graphics.Image screen, int cameraOffsetX, int cameraOffsetY)
		{
			SpriteImageData sid;
			++this.renderCounter;

			switch (this.state)
			{
				case State.Standing:
					sid = SpriteImageFactory.GetImage("link " + this.DirectionString + " 1");
					break;

				case State.Walking:
					int num = (this.lifetimeCounter / 6) % 4;
					if (num == 1 || num == 3) num = 1;
					else if (num == 2) num = 3;
					else num = 2;
					sid = SpriteImageFactory.GetImage("link " + this.DirectionString + " " + num.ToString());
					break;

				default:
					throw new InvalidOperationException("sprite render state not defined");
			}

			Image image = sid.Image;
			int offsetX = sid.OffsetX;
			int offsetY = sid.OffsetY;

			screen.Blit(image, this.RenderLeft + offsetX - cameraOffsetX, this.RenderTop + offsetY - cameraOffsetY);
		}
	}
}
