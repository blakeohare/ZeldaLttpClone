using System;
using System.Collections.Generic;
using System.Linq;
using GameLight.Graphics;
using GameLight.Input;
using GameLight.Scene;
using GameLight.Sound;
using System.Reflection;
using System.IO;

namespace Zelda.Sprites
{
	public struct SpriteImageData
	{
		public SpriteImageData(Image image, int offsetX, int offsetY)
		{
			this.Image = image;
			this.OffsetX = offsetX;
			this.OffsetY = offsetY;
		}
		public Image Image;
		public int OffsetX;
		public int OffsetY;
	}

	public static class SpriteImageFactory
	{
		private static Dictionary<string, SpriteImageData> images = new Dictionary<string, SpriteImageData>();

		static SpriteImageFactory()
		{
			CreateImages();
		}

		public static SpriteImageData GetImage(string id)
		{
			SpriteImageData img;
			if (images.TryGetValue(id, out img))
			{
				return img;
			}
			throw new InvalidOperationException("Image not found");
		}

		private static void CreateImages()
		{
			Assembly assembly = typeof(SpriteImageFactory).Assembly;
			Stream stream = assembly.GetManifestResourceStream("Zelda.Data.sprite_manifest.txt");
			System.IO.StreamReader reader = new StreamReader(stream);
			string spriteManifest = reader.ReadToEnd();
			string[] lines = spriteManifest.Split('\n');
			string trimmedLine, id;
			int locX, locY, offsetX, offsetY, width, height;
			string[] parts, offsets, location, size;

			Image canvas = new Image("Images/sprites.png");
			Image sprite;

			foreach (string line in lines)
			{
				trimmedLine = line.Trim();
				if (trimmedLine.Length > 0)
				{
					parts = trimmedLine.Split('\t');
					id = parts[0];
					location = parts[1].Split(',');
					locX = int.Parse(location[0]);
					locY = int.Parse(location[1]);
					size = parts[2].Split(',');
					width = int.Parse(size[0]);
					height = int.Parse(size[1]);

					if (parts.Length > 3)
					{
						offsets = parts[3].Split(',');
						offsetX = int.Parse(offsets[0]);
						offsetY = int.Parse(offsets[1]);
					}
					else
					{
						offsetX = 0;
						offsetY = 0;
					}

					sprite = new Image(width, height);
					sprite.Blit(canvas, -locX, -locY);
					images.Add(id, new SpriteImageData(sprite, offsetX, offsetY));
				}
			}
		}
	}
}
