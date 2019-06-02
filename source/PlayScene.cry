using System;
using System.Collections.Generic;
using System.Linq;
using GameLight.Graphics;
using GameLight.Input;
using GameLight.Scene;
using GameLight.Sound;
using Zelda.Map;

namespace Zelda
{
	public class PlayScene : GameSceneBase
	{
		private Sprites.Link link;
		private Level level;
		private int renderCounter = 0;

		public PlayScene(Level level)
		{
			this.level = level;
			TextRenderer.PurgeCache();
		}

		private int CameraOffsetX
		{
			get
			{
				int camOffsetX = (int)(this.link.X - 128);
				if (camOffsetX < 0) return 0;
				if (camOffsetX >= this.level.Width * 16 - 256) return this.level.Width * 16 - 256; // Is this off by 1? Go to the right edge of the map to find out.
				return camOffsetX;
			}
		}

		private int CameraOffsetY
		{
			get
			{
				int camOffsetY = (int)(this.link.Y - 112);
				if (camOffsetY < 0) return 0;
				if (camOffsetY >= this.level.Height * 16 - 224) return this.level.Width * 16 - 224; // Is this off by 1? Go to the right edge of the map to find out.
				return camOffsetY;
			}
		}

		protected override void Initialize()
		{
			this.link = new Sprites.Link(1288, 220, this.level, this.level.Layers[0]);
		}

		protected override void ProcessInput(InputEvent[] events)
		{
			double dx = 0;
			double dy = 0;

			if (InputManager.IsKeyPressed(Key.Up)) dy = -1;
			if (InputManager.IsKeyPressed(Key.Down)) dy = 1;
			if (InputManager.IsKeyPressed(Key.Right)) dx = 1;
			if (InputManager.IsKeyPressed(Key.Left)) dx = -1;

			this.link.SetWalkingDirection(dx * 1.7, dy * 1.7);

			foreach (InputEvent e in events)
			{
				if (e.Type == EventType.KeyDown)
				{
					if (e.Key == Key.Enter)
					{
						InventoryScreen inventory = new InventoryScreen(this);
						this.SwitchToScene(inventory);
					}
				}
			}
		}

		protected override void Update(int gameCounter)
		{
			this.link.Update();
			this.link.MoveRequest();
		}


		private int underlayOffset = -224;
		public void SetAsInactiveUnderlay(int transitionOffset)
		{
			this.underlayOffset = transitionOffset;
		}

		public void PublicRender(Image gameScreen) { this.Render(gameScreen); }

		protected override void Render(Image gameScreen)
		{
			// TODO: render other layers
			this.RenderLayer(this.level.Layers[0], gameScreen);
			this.RenderOverlay(gameScreen);

			++this.renderCounter;
		}

		private Image overlayBase = new Image("Images/overlay.png");
		private void RenderOverlay(Image screen)
		{
			int top = 224 + this.underlayOffset;
			screen.Blit(overlayBase, 12, top);
			Image rupeeCount = TextRenderer.GetOverlayNumber(GameState.Instance.Rupees, 3);
			Image bombCount = TextRenderer.GetOverlayNumber(GameState.Instance.Bombs, 2);
			Image arrowCount = TextRenderer.GetOverlayNumber(GameState.Instance.Arrows, 2);
			
			screen.Blit(rupeeCount, 65, 24 + top);
			screen.Blit(bombCount, 97, 24 + top);
			screen.Blit(arrowCount, 121, 24 + top);
		}

		private Image canopy = new Image(256, 224);

		private void RenderLayer(Layer layer, Image screen)
		{
			this.canopy.Fill(Colors.Transparent);

			int camOffsetX = this.CameraOffsetX;
			int camOffsetY = this.CameraOffsetY;

			int left = camOffsetX / 16;
			int right = left + 17;
			int top = camOffsetY / 16;
			int bottom = top + 15;
			left--;
			right++;
			top--;
			bottom++;

			left = left < 0 ? 0 : left;
			right = right >= this.level.Width ? this.level.Width - 1 : right;
			top = top < 0 ? 0 : top;
			bottom = bottom >= this.level.Height ? this.level.Height - 1 : bottom;

			int row, col;

			Tile[,] tiles = layer.Tiles;
			Image image;
			Tile tile;
			int x, y;
			bool canopyUsed = false;

			for (row = top; row <= bottom; ++row)
			{
				for (col = left; col <= right; ++col)
				{
					x = col * 16 - camOffsetX;
					y = row * 16 - camOffsetY;
					tile = tiles[col, row];
					image = tile.GetImage(this.renderCounter);
					screen.Blit(image, x, y);
					image = tile.GetCanopyImage(this.renderCounter);
					if (image != null)
					{
						this.canopy.Blit(image, x, y);
						canopyUsed = true;
					}
				}
			}

			if (this.link.Layer == layer)
			{
				this.link.Render(screen, camOffsetX, camOffsetY);
			}

			if (canopyUsed)
			{
				screen.Blit(this.canopy, 0, 0);
			}
		}
	}
}