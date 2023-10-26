/*
Auto-generated by: https://github.com/pmndrs/gltfjsx
Command: npx gltfjsx@6.2.14 public/pickleball.glb 
*/

import React, { Suspense, useEffect, useRef } from "react";
import { Canvas } from "@react-three/fiber";
import { OrbitControls, Preload, useGLTF } from "@react-three/drei";
import CanvasLoader from "./CanvasLoader";

export function Pickleball(props) {
  const { nodes, materials } = useGLTF(
    `${process.env.REACT_APP_API_HOST}/static/pickleball.glb`
  );
  const group = useRef();

  useEffect(() => {
    const handleResize = () => {
      if (window.innerWidth < 768) {
        group.current.scale.set(0.5, 0.5, 0.5);
      } else {
        group.current.scale.set(1, 1, 1);
      }
    };

    window.addEventListener("resize", handleResize);

    return () => {
      window.removeEventListener("resize", handleResize);
    };
  }, [group]);

  return (
    <Canvas
      frameloop="demand"
      shadows
      dpr={[1, 2]}
      camera={{ position: [20, 3, 5], fov: 25 }}
      gl={{ preserveDrawingBuffer: true }}
    >
      <Suspense fallback={<CanvasLoader />}>
        <OrbitControls
          enableZoom={false}
          maxPolarAngle={Math.PI / 2}
          minPolarAngle={Math.PI / 2}
        />
        <ambientLight intensity={0.5} />
        <group {...props} dispose={null}>
          <group
            position={[0.5, -0.1, -1]}
            rotation={[Math.PI / 2, 0.5, 0.5]}
            scale={36}
          >
            <mesh>
              <hemisphereLight intensity={0.6} groundColor="black" />
              <pointLight intensity={1} />
              <spotLight
                position={[-20, 50, 10]}
                angle={0.12}
                penumbra={1}
                intensity={1}
                castShadow
                shadow-mapSize={1024}
              />
              <mesh
                geometry={nodes.indoor_ball.geometry}
                material={materials.aiStandardSurface1}
                rotation={[Math.PI / 2, 0, 0]}
                scale={0.01}
              />
            </mesh>
          </group>
        </group>
      </Suspense>
      <Preload all />
    </Canvas>
  );
}

export default Pickleball;

useGLTF.preload("/pickleball.glb");
