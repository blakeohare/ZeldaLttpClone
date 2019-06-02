using System;
using System.Collections.Generic;
using System.Linq;
using GameLight.Graphics;
using GameLight.Input;
using GameLight.Scene;
using GameLight.Sound;

namespace Zelda.Map
{
	public class Level
	{
		private List<Layer> layers = new List<Layer>();
		private int width;
		private int height;

		public int Width { get { return this.width; } }
		public int Height { get { return this.height; } }

		public Level(IEnumerable<Layer> layers)
		{
			this.layers = new List<Layer>(layers);
			this.width = this.layers[0].Width;
			this.height = this.layers[0].Height;
		}

		public List<Layer> Layers { get { return this.layers; } }
	}
}
