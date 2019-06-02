/*
	TODO list:
	diagonal and corner forgiveness
	ladders
	swinging sword
	chopping grass and bushes
	hammer
	push/pull on edges
	push/pull objects
	jumping from ledges
	picking up objects
	shovel
	pegasus boots
	water
	hookshot
	bow and arrow sticking
	bomb
	falling down holes
	goodies
 */

using System;
using System.Collections.Generic;
using System.Linq;
using System.Net;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Documents;
using System.Windows.Input;
using System.Windows.Media;
using System.Windows.Media.Animation;
using Zelda.Map;

namespace Zelda
{
	public partial class MainPage : UserControl
	{
		public MainPage()
		{
			InitializeComponent();
			this.LayoutRoot.Children.Add(
				new GameLight.Scene.GameControl()
				{
					GameWidth = 256,
					GameHeight = 224,
					FullScreenShortcutKey = GameLight.Input.Key.F,
					TargetFramesPerSecond = 60,
					StartingScene = new PlayScene(LevelStore.GetLevel("lightworld"))
				});
		}
	}
}
