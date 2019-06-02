using System;
using System.Collections.Generic;
using System.Linq;
using GameLight.Graphics;
using GameLight.Input;
using GameLight.Scene;
using GameLight.Sound;

namespace Zelda.Map
{
	public class TileTemplate
	{
		private Image[] images;
		private int numImages;
		private Barrier[] barriers;
		private Barrier[] tallBarriers;
		private HashSet<string> specialCodes;

		public string ID { get; private set; }

		public Barrier[] Barriers { get { return this.barriers; } }
		public Barrier[] TallBarriers { get { return this.tallBarriers; } }

		private bool isCanopy = false;
		public bool IsCanopy { get { return this.isCanopy; } }

		public TileTemplate(string id, Image[] images, string physics, string[] specialCodes)
		{
			this.ID = id;
			this.images = images;
			this.numImages = images.Length;
			this.InitializePhysics(physics);
			this.specialCodes = new HashSet<string>(specialCodes);
			this.InitializeFlags(specialCodes);
		}

		private void InitializeFlags(string[] codes)
		{
			foreach (string code in codes)
			{
				switch (code)
				{
					case "canopy":
						this.isCanopy = true;
						break;

					case "tallgrass":
						// TODO: this
						break;

					default:
						throw new InvalidOperationException("Unrecognized code: " + code);
				}
			}
		}

		private Barrier[] GetBarrierList(string physics, int left, int top, int width, int height)
		{
			switch (physics)
			{
				case "g":
					return new Barrier[0];

				case "t":
					return new Barrier[] { new Barrier(left, top, left + width, top + height, false, false, false, false) };

				default:
					return new Barrier[0];
			}
		}

		private static int[] leftList = new int[] { 0, 8, 0, 8 };
		private static int[] topList = new int[] { 0, 0, 8, 8 };

		private void InitializePhysics(string physics)
		{
			List<Barrier> barriers = new List<Barrier>();
			List<Barrier> tallBarriers = new List<Barrier>();
			Barrier[] tempBarrierList;
			string tempPhysics;

			if (physics.Contains(','))
			{
				string[] physicses = physics.Split(',');
				for (int i = 0; i < 4; ++i)
				{
					tempPhysics = physicses[i];
					tempBarrierList = this.GetBarrierList(tempPhysics, leftList[i], topList[i], 8, 8);
					barriers.AddRange(tempBarrierList);
					if (tempPhysics == "t")
					{
						tallBarriers.AddRange(tempBarrierList);
					}
				}
			}
			else
			{
				tempBarrierList = this.GetBarrierList(physics, 0, 0, 16, 16);
				barriers.AddRange(tempBarrierList);
				if (physics == "t")
				{
					tallBarriers.AddRange(tempBarrierList);
				}
			}

			this.barriers = barriers.ToArray();
			this.tallBarriers = tallBarriers.ToArray();
		}

		public Image GetImage(int renderCounter)
		{
			return images[(renderCounter / 10) % numImages];
		}

		public bool IsAnimated
		{
			get { return this.numImages > 1; }
		}

		/// <summary>
		/// Special codes are used for identifying tile templates as having 
		/// certain properties. Such as foliage that can be chopped away. 
		/// </summary>
		public bool ContainsSpecialTile(string code)
		{
			return this.specialCodes.Contains(code);
		}
	}
}