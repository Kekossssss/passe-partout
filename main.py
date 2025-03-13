enum ActionKind {
    Walking,
    Idle,
    Jumping,
    Rotation
}
namespace SpriteKind {
    export const Bonus = SpriteKind.create()
    export const Dechets = SpriteKind.create()
    export const Environnement = SpriteKind.create()
}
sprites.onOverlap(SpriteKind.Player, SpriteKind.Bonus, function (sprite2, otherSprite2) {
    otherSprite2.destroy(effects.confetti)
    info.changeLifeBy(1)
})
sprites.onOverlap(SpriteKind.Environnement, SpriteKind.Bonus, function (sprite, otherSprite) {
    otherSprite.destroy(effects.none, 200)
})
sprites.onOverlap(SpriteKind.Environnement, SpriteKind.Enemy, function (sprite, otherSprite) {
    Destroy_joueur = 1
    otherSprite.destroy(effects.none, 200)
})
controller.A.onEvent(ControllerButtonEvent.Pressed, function () {
    if (Nb_Projectile < NB_PROJECTILE_MAX) {
        Nb_Projectile += 1
        if (Type_Projectile == 0) {
            projectile = sprites.createProjectileFromSprite(assets.image`Pierre`, ship, 0, -50)
        } else if (Type_Projectile == 1) {
            projectile = sprites.createProjectileFromSprite(assets.image`Baguette`, ship, 0, -80)
        } else if (Type_Projectile == 2) {
            projectile = sprites.createProjectileFromSprite(assets.image`piece`, ship, 0, -100)
        } else {
            projectile = sprites.createProjectileFromSprite(assets.image`boule_feu`, ship, 120, 0)
        }
        projectile.startEffect(effects.trail, 100)
    }
    pause(200)
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.Dechets, function (sprite, otherSprite) {
    Destroy_joueur = 1
    otherSprite.destroy(effects.hearts, 200)
    info.changeScoreBy(1)
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.Environnement, function (sprite, otherSprite) {
    info.changeLifeBy(-1)
    pause(2000)
})
sprites.onDestroyed(SpriteKind.Dechets, function (sprite) {
    if (Destroy_joueur == 0 && Message_N2 == 1) {
        info.changeLifeBy(-1)
    }
    Destroy_joueur = 0
})
sprites.onDestroyed(SpriteKind.Enemy, function (sprite) {
    if (Destroy_joueur == 0 && info.score() > 0) {
        info.changeScoreBy(-1)
    }
    Destroy_joueur = 0
})
sprites.onDestroyed(SpriteKind.Projectile, function (sprite) {
    if (Nb_Projectile >= 0) {
        Nb_Projectile += -1
    }
})
sprites.onOverlap(SpriteKind.Projectile, SpriteKind.Enemy, function (sprite, otherSprite) {
    Destroy_joueur = 1
    sprite.destroy()
    otherSprite.destroy(effects.disintegrate, 200)
    info.changeScoreBy(1)
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.Enemy, function (sprite, otherSprite) {
    scene.cameraShake(4, 500)
    otherSprite.destroy(effects.disintegrate, 100)
    sprite.startEffect(effects.fire, 200)
    info.changeLifeBy(-1)
})
let Vitesse_Bonus = 0
let Vitesse_Y = 0
let Vitesse_X = 0
let Indice_Projectile = 0
let Vitesse_ennemie_Y = 0
let Vitesse_ennemie_X = 0
let Taille_eau = 0
let Eau: Sprite = null
let Niveau = 0
let projectile: Sprite = null
let Type_Projectile = 0
let Nb_Projectile = 0
let Destroy_joueur = 0
let Message_N2 = 0
let NB_PROJECTILE_MAX = 0
let ship: Sprite = null
let clouds = [img`
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . b b b b b . . . . . . 
    . . . b b b b b b b b b . . . . 
    . . b b f b b b b f b b b . . . 
    . . b b f f b b f f b b b . . . 
    . . b b b b f f b b b b b . . . 
    . . b b b b 2 2 b b b b b . . . 
    . . . b b b b b b b b b . . . . 
    . . . . . b b b b b . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    `, img`
    . . . . . . . . . . . . . . . . 
    . . . 2 . . . . . . 2 . . . . . 
    . . . 2 2 . . . . 2 2 . . . . . 
    . . . 2 2 2 2 2 2 2 2 . . . . . 
    . . . . 2 1 f f 1 2 . . . . . . 
    . . . . 2 2 f f 2 2 . . . . . . 
    . . . . . 2 2 2 2 . . . . . . . 
    . . . . . . . . . . . . . . . . 
    `]
let Bonus2 = [assets.image`Pomme`, assets.image`Pizza`]
let Déchets = [assets.image`Dechet1`, assets.image`Dechet2`, assets.image`Dechet3`]
ship = sprites.create(img`
    ......ffff..............
    ....fff22fff............
    ...fff2222fff...........
    ..fffeeeeeefff..........
    ..ffe222222eef..........
    ..fe2ffffff2ef..........
    ..ffffeeeeffff......ccc.
    .ffefbf44fbfeff....cddc.
    .ffefbf44fbfeff...cddc..
    .fee4dddddd4eef.ccddc...
    fdfeeddddd4eeffecddc....
    fbffee4444ee4fddccc.....
    fbf4f222222f1edde.......
    fcf.f222222f44ee........
    .ff.f448544f............
    ....ffffffff............
    .....ff..ff.............
    ........................
    `, SpriteKind.Player)
ship.setStayInScreen(true)
ship.bottom = 120
effects.clouds.startScreenEffect(500)
tiles.setCurrentTilemap(tilemap`niveau4`)
info.setLife(3)
NB_PROJECTILE_MAX = 4
let Message_N0 = 1
let Message_N1 = 1
Message_N2 = 1
game.onUpdateInterval(5000, function () {
    if (Niveau >= 2) {
        sprites.destroy(Eau)
        Taille_eau = randint(10, 180)
        Eau = sprites.createProjectileFromSide(img`
            8 8 . . 8 8 8 . . . . . . . . 8 
            9 8 8 8 8 9 8 8 . . 8 8 8 8 8 8 
            9 9 9 9 9 9 9 9 8 8 8 9 9 9 9 9 
            9 8 8 8 9 9 9 9 9 9 9 9 9 9 9 9 
            9 9 9 8 9 9 9 9 9 9 9 9 9 9 9 9 
            9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 
            9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 
            9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 
            9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 
            9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 8 
            9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 
            9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 
            9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 
            9 9 9 9 8 9 9 9 9 9 9 9 9 9 9 9 
            9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 
            9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 
            `, 0, 0)
        Eau.setKind(SpriteKind.Environnement)
        scaling.scaleToPixels(Eau, 320, ScaleDirection.Horizontally, ScaleAnchor.Middle)
        scaling.scaleToPixels(Eau, Taille_eau, ScaleDirection.Vertically, ScaleAnchor.Middle)
        Eau.x = 0
        Eau.y = 120
    }
})
game.onUpdateInterval(5000, function () {
    projectile = sprites.createProjectileFromSide(Bonus2[randint(0, Bonus2.length - 1)], Vitesse_ennemie_X, Vitesse_ennemie_Y)
    projectile.setKind(SpriteKind.Bonus)
    if (Niveau >= 2) {
        projectile.x = 150
        projectile.y = randint(10, 150)
    } else {
        projectile.x = randint(10, 150)
    }
})
game.onUpdateInterval(700, function () {
    if (Niveau == 1) {
        Indice_Projectile = randint(0, Déchets.length - 1)
        projectile = sprites.createProjectileFromSide(Déchets[Indice_Projectile], Vitesse_ennemie_X, Vitesse_ennemie_Y)
        projectile.setKind(SpriteKind.Dechets)
        projectile.x = randint(10, 150)
        if (Indice_Projectile == 0) {
            animation.runImageAnimation(
            projectile,
            assets.animation`myAnim1`,
            500,
            true
            )
        } else if (Indice_Projectile == 1) {
            animation.runImageAnimation(
            projectile,
            assets.animation`myAnim2`,
            500,
            true
            )
        } else {
            animation.runImageAnimation(
            projectile,
            assets.animation`myAnim3`,
            500,
            true
            )
        }
    }
})
game.onUpdateInterval(1000, function () {
    if (Niveau >= 2) {
        projectile = sprites.createProjectileFromSide(clouds[randint(0, clouds.length - 1)], Vitesse_ennemie_X, Vitesse_ennemie_Y)
        projectile.setKind(SpriteKind.Enemy)
        projectile.x = 160
        projectile.y = randint(10, 150)
        projectile = sprites.createProjectileFromSide(clouds[randint(0, clouds.length - 1)], Vitesse_ennemie_X, Vitesse_ennemie_Y)
        projectile.setKind(SpriteKind.Enemy)
        projectile.x = 160
        projectile.y = randint(10, 150)
    }
})
game.onUpdateInterval(800, function () {
    if (Niveau == 0) {
        projectile = sprites.createProjectileFromSide(clouds[randint(0, clouds.length - 1)], Vitesse_ennemie_X, Vitesse_ennemie_Y)
        projectile.setKind(SpriteKind.Enemy)
        projectile.x = randint(10, 150)
    }
})
forever(function () {
    controller.moveSprite(ship, Vitesse_X, Vitesse_Y)
    if (game.runtime() <= 10000) {
        Niveau = 0
    } else if (game.runtime() <= 30000) {
        Niveau = 1
    } else {
        Niveau = 2
    }
    if (Niveau == 0) {
        Type_Projectile = 0
        Vitesse_Bonus = 30
        Vitesse_ennemie_X = 0
        Vitesse_ennemie_Y = 30
        Vitesse_X = 100
        Vitesse_Y = 0
        scene.setBackgroundImage(assets.image`Mont_Fuji`)
        ship.setImage(img`
            . . . . . . 5 . 5 . . . . . . . 
            . . . . . f 5 5 5 f f . . . . . 
            . . . . f 1 5 2 5 1 6 f . . . . 
            . . . f 1 6 6 6 6 6 1 6 f . . . 
            . . . f 6 6 f f f f 6 1 f . . . 
            . . . f 6 f f d d f f 6 f . . . 
            . . f 6 f d f d d f d f 6 f . . 
            . . f 6 f d 3 d d 3 d f 6 f . . 
            . . f 6 6 f d d d d f 6 6 f . . 
            . f 6 6 f 3 f f f f 3 f 6 6 f . 
            . . f f d 3 5 3 3 5 3 d f f . . 
            . . f d d f 3 5 5 3 f d d f . . 
            . . . f f 3 3 3 3 3 3 f f . . . 
            . . . f 3 3 5 3 3 5 3 3 f . . . 
            . . . f f f f f f f f f f . . . 
            . . . . . f f . . f f . . . . . 
            `)
    } else if (Niveau == 1) {
        Type_Projectile = 2
        Vitesse_Bonus = 50
        Vitesse_ennemie_X = 0
        Vitesse_ennemie_Y = 50
        Vitesse_X = 150
        Vitesse_Y = 0
        scene.setBackgroundImage(assets.image`Ville`)
        ship.setImage(img`
            . . . . f f f f . . . . 
            . . f f e e e e f f . . 
            . f f e e e e e e f f . 
            f f f f 4 e e e f f f f 
            f f f 4 4 4 e e f f f f 
            f f f 4 4 4 4 e e f f f 
            f 4 e 4 4 4 4 4 4 e 4 f 
            f 4 4 f f 4 4 f f 4 4 f 
            f e 4 d d d d d d 4 e f 
            . f e d d b b d d e f . 
            . f f e 4 4 4 4 e f f . 
            e 4 f b 1 1 1 1 b f 4 e 
            4 d f 1 1 1 1 1 1 f d 4 
            4 4 f 6 6 6 6 6 6 f 4 4 
            . . . f f f f f f . . . 
            . . . f f . . f f . . . 
            `)
    } else {
        Type_Projectile = 4
        Vitesse_Bonus = 60
        Vitesse_ennemie_X = -30
        Vitesse_ennemie_Y = 0
        Vitesse_X = 100
        Vitesse_Y = 100
        scene.setBackgroundImage(assets.image`Ciel`)
        ship.setImage(img`
            ..ccc.........ffffff....
            ..f4cc.......fcc22ff....
            ..f44cc...fffccccff.....
            ..f244cccc22224442cc....
            ..f224cc2222222244b9c...
            ..cf2222222222222b999c..
            .c22c222222222b11199b2c.
            f22ccccccc222299111b222c
            fffffcc222c222222222222f
            .....f2222442222222222f.
            ....f222244fc2222222ff..
            ...c222244ffffffffff....
            ...c2222cfffc2f.........
            ...ffffffff2ccf.........
            .......ffff2cf..........
            ........fffff...........
            `)
    }
    if (info.life() > 5) {
        info.setLife(5)
    }
    if (Niveau == 0 && Message_N0 == 1) {
        game.showLongText("Eliminez les ennemis !", DialogLayout.Center)
        sprites.destroyAllSpritesOfKind(SpriteKind.Enemy)
        sprites.destroyAllSpritesOfKind(SpriteKind.Projectile)
        sprites.destroyAllSpritesOfKind(SpriteKind.Bonus)
        Message_N0 = 0
    } else if (Niveau == 1 && Message_N1 == 1) {
        game.showLongText("Ne laissez pas les déchets toucher le sol !", DialogLayout.Center)
        sprites.destroyAllSpritesOfKind(SpriteKind.Enemy)
        Message_N1 = 0
    } else if (Niveau == 2 && Message_N2 == 1) {
        game.showLongText("Frayez-vous un chemin à travers les ennemies !", DialogLayout.Center)
        Message_N2 = 0
        sprites.destroyAllSpritesOfKind(SpriteKind.Dechets)
    } else {
    	
    }
})
