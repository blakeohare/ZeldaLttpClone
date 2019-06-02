using System;
using System.Collections.Generic;
using System.Linq;
using System.IO;
using System.Reflection;
using GameLight.Graphics;
using GameLight.Input;
using GameLight.Scene;
using GameLight.Sound;

namespace Zelda.Map
{
	public class TileFactory
	{
		private Dictionary<string, TileTemplate> templates = new Dictionary<string, TileTemplate>();

		static TileFactory()
		{
			Instance = new TileFactory();
		}
		public static TileFactory Instance { get; private set; }
		private TileFactory()
		{
			this.InitializeTileImages();
		}

		private void InitializeTileImages()
		{
			Assembly assembly = typeof(TileFactory).Assembly;
			System.IO.Stream stream = assembly.GetManifestResourceStream("Zelda.Data.tile_manifest.txt");
			System.IO.StreamReader streamReader = new StreamReader(stream);
			string[] lines = streamReader.ReadToEnd().Trim().Split('\n');

			string[] parts;
			string id, physics;
			string[] images, codes;
			int col, row, i;
			string[] imageCoords;

			Image tileSource = new Image("images/tiles.png");
			Image[] animation;
			int animationLength;
			string[] emptyCodes = new string[0];

			foreach (string line in lines)
			{
				parts = line.Trim().Split('\t');
				id = parts[0];
				physics = parts[1];
				images = parts[2].Split('|');
				animationLength = images.Length;
				animation = new Image[animationLength];
				codes = parts.Length == 4 ? parts[3].Split(',') : emptyCodes;
				for (i = 0; i < animationLength; ++i)
				{
					imageCoords = images[i].Split(',');
					col = int.Parse(imageCoords[0]);
					row = int.Parse(imageCoords[1]);
					animation[i] = new Image(16, 16);
					animation[i].Blit(tileSource, -col * 16, -row * 16);
				}

				this.templates.Add(id, new TileTemplate(id, animation, physics, codes));
			}
		}

		public TileTemplate GetTemplate(string id)
		{
			// I want unknown ID's to throw
			return templates[id];
		}

		private TileTemplate[] tt = new TileTemplate[10];
		public Tile GenerateTile(int col, int row, params string[] ids)
		{
			int idsLength = ids.Length;
			for (int i = 0; i < 10; ++i)
			{
				if (i < idsLength)
				{
					tt[i] = templates[ids[i]];
				}
				else
				{
					tt[i] = null;
				}
			}

			return new Tile(col, row, tt);
		}
	}
}
