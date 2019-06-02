using System;
using System.Collections.Generic;
using System.Linq;
using GameLight.Graphics;
using GameLight.Input;
using GameLight.Scene;
using GameLight.Sound;

namespace Zelda.Map
{
	public class Tile
	{
		private List<TileTemplate> templates = new List<TileTemplate>();

		private Barrier[] barriers = null;
		private bool empty;
		private bool animated;
		private Image flattenedImage = new Image(16, 16);
		private int col;
		private int row;
		private PhysicsTypes[] physics;

		public Tile(int col, int row, TileTemplate[] templates)
		{
			this.col = col;
			this.row = row;
			this.Initialize(templates);
		}

		public void InitializeBarriers()
		{
			List<Barrier> barriers = new List<Barrier>();
			foreach (TileTemplate template in this.templates)
			{
				foreach (Barrier barrier in template.Barriers)
				{
					barriers.Add(barrier.Clone(this.col, this.row));
				}
			}
			this.barriers = barriers.ToArray();
		}
		
		public bool IsCollisionWithRectangle(int left, int top, int right, int bottom)
		{
			if (this.barriers == null) this.InitializeBarriers();
			foreach (Barrier barrier in this.barriers)
			{
				if (barrier.IntersectsRectangle(left, top, right, bottom))
				{
					return true;
				}
			}
			return false;
		}

		private void Initialize(TileTemplate[] templates)
		{
			this.physics = new PhysicsTypes[] { PhysicsTypes.Ground, PhysicsTypes.Ground, PhysicsTypes.Ground, PhysicsTypes.Ground };

			bool animated = false;
			foreach (TileTemplate template in templates)
			{
				if (template == null) break;

				this.templates.Add(template);
				animated = animated || template.IsAnimated;
				this.hasCanopy = this.hasCanopy || template.IsCanopy;
			}

			this.empty = this.templates.Count == 0;
			if (!this.empty)
			{
				this.flattenedImage = new Image(16, 16);
			}
			this.animated = animated;
			if (!this.animated)
			{
				foreach (TileTemplate template in this.templates)
				{
					this.flattenedImage.Blit(template.GetImage(0), 0, 0);
				}
			}
		}

		public Image GetImage(int renderCounter)
		{
			if (this.animated)
			{
				foreach (TileTemplate template in this.templates)
				{
					this.flattenedImage.Blit(template.GetImage(renderCounter), 0, 0);
				}
			}

			return this.flattenedImage;
		}

		private Image canopyImage = null;
		private bool hasCanopy = false;

		// TODO: will the canopy ever be animated?
		// if so, this should probably cache just the canopy templates instead and then
		// return the image as a function of those per renderCounter
		public Image GetCanopyImage(int renderCounter)
		{
			if (this.hasCanopy)
			{
				if (this.canopyImage == null)
				{
					this.canopyImage = new Image(16, 16);
					foreach (TileTemplate template in this.templates)
					{
						if (template.IsCanopy)
						{
							this.canopyImage.Blit(template.GetImage(renderCounter), 0, 0);
						}
					}
				}
				return this.canopyImage;
			}
			return null;
		}

		public string[] ReplaceTemplateWithCode(string code, string newTemplateId)
		{
			List<string> newTemplates = new List<string>();

			bool found = false;
			foreach (TileTemplate template in this.templates)
			{
				if (template.ContainsSpecialTile(code))
				{
					found = true;
					if (newTemplateId != null)
					{
						newTemplates.Add(newTemplateId);
					}
				}
				else
				{
					newTemplates.Add(template.ID);
				}
			}

			return found
				? newTemplates.ToArray()
				: null;
		}

		public string[] RemoveTemplateWithCode(string code)
		{
			return this.ReplaceTemplateWithCode(code, null);
		}
	}
}
