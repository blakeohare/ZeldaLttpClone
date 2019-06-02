using System;
using System.Collections.Generic;
using System.Linq;
using System.IO;
using GameLight.Graphics;
using GameLight.Input;
using GameLight.Scene;
using GameLight.Sound;

namespace Zelda.Map
{
	public class ProtoLevel
	{
		private List<List<TileTemplate[]>> layers = new List<List<TileTemplate[]>>();
		public int Width { get; private set; }
		public int Height { get; private set; }

		public ProtoLevel(string levelName)
		{
			Dictionary<string, string> values = new Dictionary<string, string>();
			StreamReader stream = new StreamReader(typeof(ProtoLevel).Assembly.GetManifestResourceStream("Zelda.Data.Maps." + levelName + ".txt"));
			string[] lines = stream.ReadToEnd().Trim().Split('\n');
			string value, key, formatted;
			string[] parts;
			int i;

			foreach (string line in lines)
			{
				formatted = line.Trim();
				if (!string.IsNullOrEmpty(formatted) && formatted[0] == '#')
				{
					parts = formatted.Split(':');
					if (parts.Length > 1)
					{
						key = parts[0].Substring(1);
						if (!string.IsNullOrEmpty(key))
						{
							// not using string builder as this will rarely have more than a few colons
							value = parts[1];
							for (i = 2; i < parts.Length; ++i)
							{
								value += ":" + parts[i];
							}

							values[key] = value;
						}
					}
				}
			}

			this.Width = int.Parse(values["width"]);
			this.Height = int.Parse(values["height"]);

			int layerNum = 1;
			int x, y, index;
			int width = this.Width;
			int height = this.Height;
			string[] templateIds;
			TileFactory tileFactory = TileFactory.Instance;
			
			while (values.ContainsKey("layer" + layerNum.ToString()))
			{
				List<TileTemplate[]> tiles = new List<TileTemplate[]>();
				TileTemplate[] tile;
				string[] tileIdClumps = values["layer" + layerNum.ToString()].Split(',');

				for (y = 0; y < height; ++y)
				{
					for (x = 0; x < width; ++x)
					{
						index = y * width + x;
						templateIds = tileIdClumps[index].Split('|');
						tile = new TileTemplate[templateIds.Length];
						for (i = 0; i < templateIds.Length; ++i)
						{
							tile[i] = tileFactory.GetTemplate(templateIds[i]);
						}
						tiles.Add(tile);
					}
				}

				this.layers.Add(tiles);

				++layerNum;
			}
		}

		public Level GenerateNewLevel()
		{
			List<Layer> layers = new List<Layer>();
			foreach (List<TileTemplate[]> protoLayer in this.layers)
			{
				Tile[,] tiles = new Tile[this.Width, this.Height];
				int x, y, index;
				int width = this.Width;
				int height = this.Height;

				for (y = 0; y < height; ++y)
				{
					for (x = 0; x < width; ++x)
					{
						index = y * width + x;
						tiles[x, y] = new Tile(x, y, protoLayer[index]);
					}
				}
				layers.Add(new Layer(this.Width, this.Height, tiles));
			}

			return new Level(layers);
		}
	}
}
